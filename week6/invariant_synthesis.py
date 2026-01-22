# i'm not exactly following the spec for this week in terms of functions.
# but this effectively does the same thing
import os
from z3 import Solver, Int, Real, sat, unsat, Not
from sympy import Symbol, parse_expr, itermonomials, lambdify, total_degree, Poly, sympify, expand, Eq, nsimplify, gcd
import time
from itertools import combinations
import numpy as np
from week5 import parser
from functools import reduce
from ast import literal_eval
from sympy.printing.str import StrPrinter

# [AI Disclosure - Printing Assist]
class DafnyPrinter(StrPrinter):
    def _print_Pow(self, expr):
        if expr.exp.is_integer and expr.exp > 0:
            return "*".join([self.parenthesize(expr.base, 40)] * int(expr.exp))
        return super()._print_Pow(expr) # pyright: ignore[reportAttributeAccessIssue] 

# [AI Disclosure - Printing Assist]
def to_dafny(expr):
    return DafnyPrinter().doprint(expr)

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
                    degree,
                    assume_int = True
                    ):

    vars_sym = list(vars_sym)
    vars_init = list(vars_init)
    vars_trans = list(vars_trans)
    
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
    precon_vec.extend(lhs_leq_zero_form(preconditions, assume_int))
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
    
    loop_conditions = lhs_leq_zero_form(loop_conditions, assume_int)
    path_guards = lhs_leq_zero_form(path_guards, assume_int)

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

def pythonise_invariant(coeffs):
    pythonised_coeffs = []
    for a in coeffs:
        a = a.as_decimal(10)
        a = a.replace('?', '')
        a = float(a)
        pythonised_coeffs.append(a)
        
    return pythonised_coeffs

def intify(coeffs:list[float]):
    coeffs_sym = [nsimplify(coeff, tolerance=1e-10) for coeff in coeffs]
    gcd_all = reduce(gcd, coeffs_sym)

    while gcd_all != 1:
        coeffs_sym = [coeff/gcd_all for coeff in coeffs_sym]
        gcd_all = reduce(gcd, coeffs_sym)
    
    return [int(coeff) for coeff in coeffs_sym]

def is_valid_invariant(coeffs: list[int]|list[float], 
                       preconditions, loop_conditions, 
                       loop_path, vars_sym, vars_init, 
                       vars_trans, params, assume_int = True):
    
    vars_sym = list(vars_sym)
    vars_init = list(vars_init)
    vars_trans = list(vars_trans)
    
    var_data = loop_path.get('updates')
    path_guards = loop_path.get('guards')

    degree = int()
    namespace = dict()
    if assume_int:
        params_dict = {param.get('name') : Int(param.get('name')) for param in params}
        vars_dict = {var.get('name') : Int(var.get('name')) for var in var_data}
        
        namespace.update(params_dict)
        namespace.update(vars_dict)
    else:
        params_dict = {param.get('name') : Real(param.get('name')) for param in params}
        vars_dict = {var.get('name') : Real(var.get('name')) for var in var_data}

        namespace.update(params_dict)
        namespace.update(vars_dict)

    namespace['__builtins__'] = None

    precondition_constraints = []
    for precondition in preconditions:
        precondition = eval(precondition, namespace)
        precondition_constraints.append(precondition)
    
    loop_constraints = []
    for loop_condition in loop_conditions:
        loop_condition = eval(loop_condition, namespace)
        loop_constraints.append(loop_condition)
    
    for path_guard in path_guards:
        path_guard = eval(path_guard, namespace)
        loop_constraints.append(path_guard)

    degree = len(vars_dict)
    b_v_sym = sorted(list(itermonomials(vars_sym, degree)), 
                   key=lambda m: (total_degree(m), str(m)))
    
    apply_basis = lambdify(vars_sym, b_v_sym, 'numpy')
    b_v_init = apply_basis(*vars_init)

    transition_map = dict(zip([str(var_sym) for var_sym in vars_sym],
                              [str(var_trans) for var_trans in vars_trans]))
    
    b_v_z3 = []
    b_v_z3_trans = []
    for mono in b_v_sym:
        term = 1
        term_trans = 1
        if not mono.is_constant():
            powers = mono.as_powers_dict()
            for var_sym, exponent in powers.items():
                var_z3 = namespace[str(var_sym)]
                var_trans_z3 = eval(transition_map[str(var_sym)], namespace)
                term = term * (var_z3 ** exponent)
                term_trans = term_trans * (var_trans_z3 ** exponent)
        b_v_z3.append(term)
        b_v_z3_trans.append(term_trans)
    
    if assume_int:
        param_list = [Int(param.get('name')) for param in params]
    else:
        param_list = [Real(param.get('name')) for param in params]

    for param in param_list:
        b_v_init.append(param)
        b_v_z3.append(param)
        b_v_z3_trans.append(param)
    
    c = np.array(coeffs)

    inv_init = c.T @ b_v_init <= 0
    inv_curr = c.T @ b_v_z3 <= 0
    inv_next = c.T @ b_v_z3_trans <= 0

    sol = Solver()
    sol.add(precondition_constraints)

    # given the precondition, 
    # if there exists a setup where the negation of the invariant holds,
    # then the invariant is false
    sol.push()
    sol.add(Not(inv_init))
    if sol.check() == sat:
        return False
    sol.pop()

    # given the precondition, loop condition + ITE guards, and the previous invariant 
    # if there exists a setup where the negation of the next invariant holds,
    # then the invariant is false
    sol.push()
    sol.add(loop_constraints)
    sol.add(inv_curr)
    sol.add(Not(inv_next))
    if sol.check() == sat:
        return False
    sol.pop()

    return True

def get_z3_basis(params, loop_path, vars_sym, assume_int = True):

    var_data = loop_path.get('updates')

    degree = int()
    namespace = dict()
    if assume_int:
        params_dict = {param.get('name') : Int(param.get('name')) for param in params}
        vars_dict = {var.get('name') : Int(var.get('name')) for var in var_data}
        
        namespace.update(params_dict)
        namespace.update(vars_dict)
    else:
        params_dict = {param.get('name') : Real(param.get('name')) for param in params}
        vars_dict = {var.get('name') : Real(var.get('name')) for var in var_data}

        namespace.update(params_dict)
        namespace.update(vars_dict)

    namespace['__builtins__'] = None
    degree = len(vars_dict)

    b_v_sym = sorted(list(itermonomials(vars_sym, degree)), 
                   key=lambda m: (total_degree(m), str(m)))
    
    b_v_z3 = []
    for mono in b_v_sym:
        term = 1
        if not mono.is_constant():
            powers = mono.as_powers_dict()
            for var_sym, exponent in powers.items():
                var_z3 = namespace[str(var_sym)]
                term = term * (var_z3 ** exponent)
        b_v_z3.append(term)
    
    if assume_int:
        param_list = [Int(param.get('name')) for param in params]
    else:
        param_list = [Real(param.get('name')) for param in params]

    for param in param_list:
        b_v_z3.append(param)
    
    return np.array(b_v_z3)

def get_sympy_basis(params, vars_sym):
    degree = len(vars_sym)
    b_v_sym = sorted(list(itermonomials(vars_sym, degree)), 
                   key=lambda m: (total_degree(m), str(m)))
    
    param_list = [Symbol(param.get('name')) for param in params]
    for param in param_list:
        b_v_sym.append(param)

    return b_v_sym
    
def prune(coeff_list:list[list[float]|list[int]], b):
    coeff_list =  list(coeff_list)

    invariants = [b.T @ coeff <= 0 for coeff in coeff_list]

    sol = Solver()
    i = 0
    while i < len(invariants):
        inv = invariants[i]

        others = invariants[:i] + invariants[i+1:]

        if not others:
            i += 1
            continue

        sol.push()

        # we want to check if, for all bases, others ==> inv. is valid . others ==> inv == not others or inv
        # in other words, this is a check to say- the stamement "there exists some basis where other =/=> inv (others and not inv)
        # is unsat.
         
        sol.add(others)
        sol.add(Not(inv))
        if sol.check() == unsat:
            invariants.pop(i)
            coeff_list.pop(i)
        else:
            i += 1
        
        sol.pop()
    
    return coeff_list

def get_str_print_invariants(invariant_coeffs, b):
    invariant_strings = []
    for coeffs in invariant_coeffs:
        c = np.array(coeffs)
        inv = nsimplify(c.T @ b) <= 0 # pyright: ignore[reportOperatorIssue]
        inv = to_dafny(inv)
        print(f"\t\t\t>>>> [{inv}]")
        invariant_strings.append(str(inv))
    return invariant_strings

def analyze_invariants(found_floats:list[list[float]], 
                       preconditions, loop_conditions, 
                       loop_path, vars_sym, vars_init, 
                       vars_trans, params, assume_int = True):
    
    validated = set()

    for inv in found_floats:
        if assume_int:
            inv = intify(inv)

        if inv == [0]*len(inv) or inv == [-1,] + [0]*(len(inv)-1): 
            # skip trivial invariant with [0, 0 , ... , 0] or [-1, 0, 0, ... , 0]
            continue
        
        flip = [-coeff for coeff in inv]
        if is_valid_invariant(inv, preconditions, loop_conditions, 
                       loop_path, vars_sym, vars_init, 
                       vars_trans, params, assume_int):

            validated.add(str(inv))
            if is_valid_invariant(flip, preconditions, loop_conditions, 
                        loop_path, vars_sym, vars_init, 
                        vars_trans, params, assume_int):
                validated.add(str(flip))
        else:
            pass

    validated_list = [literal_eval(inv_str) for inv_str in validated]
    print("\t\t>>> Validated Invariants.")

    b_v_z3 = get_z3_basis(params, loop_path, vars_sym, assume_int = True)
    b_v_sym = get_sympy_basis(params, vars_sym)

    final_invariants = prune(validated_list, b_v_z3)


    print(f"\t\t>>> Pruned {len(found_floats) - len(final_invariants)} Invariants.")
    print()
    print('\t\t>>> Invariants:')
    get_str_print_invariants(final_invariants, b_v_sym)

    return final_invariants

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

    found_strs = set()
    found_floats = []

    print("\t\t>>> Generating Invariants...")
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

                    if str(c_s) not in found_strs:
                        print("\t\t\t>>>> Found Coefficients:", c_s)
                        found_strs.add(str(c_s))
                        found_floats.append(pythonise_invariant(c_s))
                    
                    λt_s = m[λt]
                    sol.add(λt <= λt_s - epsilon) # pyright: ignore[reportOperatorIssue]
                    sol.add(c_s.T @ c <= threshold)

                curr = time.time()

            sol.pop()

    sol.pop()

    print(f"\t\t>>> Found {len(found_floats)} Invariants.")
    print()
    return found_floats

def process_all(params, preconditions, loops, degree, assume_int = True):
    start_time = time.time()
    loop_count = 1
    for loop in loops:
        print(f"> Analyzing Loop {loop_count}...")
        loop_conditions = loop.get("conditions")
        paths = loop.get('paths')
        path_count = 1
        for loop_path in paths:
            print(f"\t>> Analyzing Path {path_count}...")
            print()
            path_guards = loop_path.get('guards')
            vars_sym, vars_init, vars_trans = parse_vars(loop_path)


            path_setup = constraints_and_setup(vars_sym, 
                                             vars_init, 
                                             vars_trans, 
                                             params, 
                                             preconditions,
                                             loop_conditions,
                                             path_guards,
                                             degree,
                                             assume_int)
            found_floats = solve(*path_setup)

            analyze_invariants(found_floats, preconditions, loop_conditions, loop_path,
                               vars_sym, vars_init, vars_trans, params, assume_int)
            path_count += 1
            print()
        
        loop_count += 1
        print()
    
    end_time = time.time()
    print(f"> Finished in {format(end_time - start_time, '.2f')}s")
        
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_file = os.path.join(current_dir, 'test.dfy')
    params, preconditions, loops = load_data(target_file, method_id=0)
    process_all(params, preconditions, loops, degree=2)