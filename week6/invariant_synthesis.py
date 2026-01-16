# i'm not exactly following the spec for this week in terms of functions.
# but this effectively does the same thing
import os

from z3 import Solver, Real, sat
from sympy import Symbol, parse_expr, itermonomials, lambdify, total_degree, Poly, sympify, expand, Eq
import time
from itertools import combinations
import numpy as np
from week5 import parser
import json

def load_data(filename:str, method_id = 0):
    parsed_data = parser.parse_file(filename)
    method = parsed_data[method_id]
    params = method.get('parameters')
    preconditions = method.get('preconditions')
    loops = method.get('loops')
    return params, preconditions, loops


def parse_vars(loop_path):
    vars_sym = []
    vars_init = []
    vars_trans = []
    var_data = loop_path.get('updates')

    for var in var_data:
        var_sym = Symbol(var.get('name'))
        vars_sym.append(var_sym)

        var_init = int(var.get('init'))
        vars_init.append(var_init)

        var_trans = parse_expr(var.get('trans'))
        vars_trans.append(var_trans)
    
    return vars_sym, vars_init, vars_trans

def lhs_leq_zero_form(inequalities, assume_int=True):
    parsed_ineqs = []
    
    for cond in inequalities:
        strict_offset = 1 if assume_int else 0
        
        if "==" in cond:
            lhs, rhs = cond.split("==")
            lhs, rhs = sympify(lhs), sympify(rhs)
            parsed_ineqs.extend([lhs - rhs, rhs - lhs])
            
        elif "<=" in cond:
            lhs, rhs = cond.split("<=")
            lhs, rhs = sympify(lhs), sympify(rhs)
            parsed_ineqs.append(lhs - rhs)
            
        elif ">=" in cond:
            lhs, rhs = cond.split(">=")
            lhs, rhs = sympify(lhs), sympify(rhs)
            parsed_ineqs.append(rhs - lhs)
            
        elif "<" in cond:
            lhs, rhs = cond.split("<")
            lhs, rhs = sympify(lhs), sympify(rhs)
            parsed_ineqs.append((lhs - rhs) + strict_offset)
            
        elif ">" in cond:
            lhs, rhs = cond.split(">")
            lhs, rhs = sympify(lhs), sympify(rhs)
            parsed_ineqs.append((rhs - lhs) + strict_offset)
            
    return parsed_ineqs

def coeff_matching_conditions(lhs, rhs):
    all_monomials = set(lhs.monoms()).union(set(rhs.monoms()))

    equalities = []
    for monom in sorted(all_monomials):
        eq_lhs = lhs.coeff_monomial(monom)
        eq_rhs = rhs.coeff_monomial(monom)

        equality = Eq(eq_lhs, eq_rhs)
        equalities.append(equality)

    return equalities

def get_precondition_constraints(equalities, c, λp):
    namespace = {f"a{i}" : c[i] for i in range(len(c))}
    namespace.update({f"λp{i}" : λp[i] for i in range(len(λp))})

    precondition_constraints = []
    for equality in equalities:
        lhs = equality.lhs
        rhs = equality.rhs

        equality = str(lhs) + " == " + str(rhs)
        constraint = eval(equality, {"__builtins__": {}}, namespace)
        precondition_constraints.append(constraint)
    
    return precondition_constraints

def write_expression_as_basis_vector(expr, vars_sym, b_v):
    return [int(Poly(expr, *vars_sym).coeff_monomial(mono)) for mono in b_v]


def constraints_and_setup(
                    vars_sym, 
                    vars_init, 
                    vars_trans, 
                    params, 
                    preconditions,
                    loop_conditions,
                    path_guards,
                    degree
                    ):
    
    b_v = sorted(list(itermonomials(vars_sym, degree)), 
                   key=lambda m: (total_degree(m), str(m)))
    
    apply_basis = lambdify(vars_sym, b_v, 'numpy')
    b_v_init = apply_basis(*vars_init)
    b_v_init_sym = apply_basis(*vars_init)
    b_v_init_const = apply_basis(*vars_init)

    M = []
    for ele in b_v:
        expr = ele.subs(list(zip(vars_sym, vars_trans)))
        trans_vec = write_expression_as_basis_vector(expr, vars_sym, b_v)
        M.append(trans_vec)
    M = np.array(M)

    for param in params:
        param = param.get('name')
        param_sym = Symbol(param)
        b_v_init_sym.append(param_sym)
        b_v.append(param_sym)
        vars_sym.append(param_sym)

        param = Real(f'{param}')
        b_v_init.append(param)
        b_v_init_const.append(0)

        M = np.pad(M, ((0, 1), (0, 1)))
        M[-1, -1] = 1
    
    k = len(b_v_init_sym)
    coeff_indices = range(k)

    params_sym = [Symbol(param.get('name')) for param in params]
    c = np.array([Symbol(f'a{i}') for i in coeff_indices])
    lhs = c.T @ b_v_init_sym
    lhs = Poly(lhs, params_sym)

    precon_vec = [-1]
    precon_vec.extend(lhs_leq_zero_form(preconditions))
    λp = np.array([Symbol(f'λp{i}') for i in range(len(preconditions)+1)])
    rhs = λp.T @ precon_vec
    rhs = expand(rhs)
    rhs = Poly(rhs, params_sym)

    equalities = coeff_matching_conditions(lhs, rhs)
    c = np.array([Real(f'a{i}') for i in coeff_indices])
    λp = np.array([Real(f'λp{i}') for i in range(len(preconditions)+1)])

    norm_constraint = c.T @ c == 1
    precondition_constraint = get_precondition_constraints(equalities, c, λp)

    lhs = M.T @ c

    λc = Real('λc')
    λt = Real('λt')
    
    loop_conditions = lhs_leq_zero_form(loop_conditions)
    path_guards = lhs_leq_zero_form(path_guards)

    loop_cond_vecs = np.array([write_expression_as_basis_vector(expr, vars_sym, b_v) for expr in loop_conditions])
    path_guard_vecs = np.array([write_expression_as_basis_vector(expr, vars_sym, b_v) for expr in path_guards])

    λl = np.array([Real(f'λl{i}') for i in range(len(loop_conditions))])
    λg = np.array([Real(f'λg{i}') for i in range(len(path_guards))])
    
    t = np.array([-1 if i == 0 else 0 for i in coeff_indices])

    if len(loop_conditions) > 0:
        term_loop = λl.T @ loop_cond_vecs
    else:
        term_loop = np.zeros(k, dtype=object)

    if len(path_guards) > 0:
        term_path = λg.T @ path_guard_vecs
    else:
        term_path = np.zeros(k, dtype=object)

    rhs = c*λc + term_loop + term_path + t*λt

    farkas_constraints = [lhs[i] == rhs[i]  for i in coeff_indices]

    lambda_constraints = [λc >= 0, λt >= 0]
    lambda_constraints.extend([λp[i] >= 0 for i in range(len(λp))])
    lambda_constraints.extend([λl[i] >= 0 for i in range(len(λl))])
    lambda_constraints.extend([λg[i] >= 0 for i in range(len(λg))])

    return norm_constraint, precondition_constraint, farkas_constraints, lambda_constraints, c, λt

def solve(norm_constraint, 
          precondition_constraint, 
          farkas_constraints, 
          lambda_constraints,
          c,
          λt):
    
    k = len(c)
    coeff_indices = range(k)
    sol = Solver()
    sol.add(norm_constraint)

    sol.add(precondition_constraint)
    sol.add(farkas_constraints)
    sol.add(lambda_constraints)

    sol.set('timeout', 100)

    epsilon = 0.01
    threshold = 0.866

    sol.push()

    found = set()
    for choice_count in range(1, k+1):
        for active_coeffs in combinations(coeff_indices, choice_count):

            #print("Active:", [c[i] for i in active_coeffs])
            inactive_coeffs = [c[i] == 0 for i in coeff_indices if i not in active_coeffs]
            sol.push()
            sol.add(inactive_coeffs)

            curr = time.time()
            end = curr + 1

            while curr < end:
                if sol.check() == sat:
                    m = sol.model()
                    c_s = np.array([m[coeff] for coeff in c])

                    if str(c_s) not in found:
                        print("Found Solution:", c_s)
                        found.add(str(c_s))
                    
                    λt_s = m[λt]
                    sol.add(λt <= λt_s - epsilon)
                    sol.add(c_s.T @ c <= threshold)

                curr = time.time()

            sol.pop()

    sol.pop()
    #return found

def process_all(params, preconditions, loops, degree):
    for loop in loops:
        loop_conditions = loop.get("conditions")
        paths = loop.get('paths')
        for loop_path in paths:
            path_guards = loop_path.get('guards')
            vars_sym, vars_init, vars_trans = parse_vars(loop_path)
            path_setup = constraints_and_setup(vars_sym, 
                                             vars_init, 
                                             vars_trans, 
                                             params, 
                                             preconditions,
                                             loop_conditions,
                                             path_guards,
                                             degree)
            solve(*path_setup)
        
if __name__ == "__main__":
    # Get the directory where THIS script is located (week6/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Join it with the filename
    target_file = os.path.join(current_dir, 'test.dfy')

    # Pass the full path to your function
    params, preconditions, loops = load_data(target_file, method_id=0)
    
    # Process the data...
    process_all(params, preconditions, loops, degree=2)