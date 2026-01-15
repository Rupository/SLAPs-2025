# i'm not exactly following the spec for this week in terms of functions.
# but this effectively does the same thing

from z3 import Solver, Real as z3Real, Reals as z3Reals, sat
from sympy import Symbol, symbols, parse_expr, itermonomials, lambdify, total_degree, Poly
import time
from itertools import combinations
import numpy as np
from week5 import parser

import json


def load_data(filename:str, method_id = 0):
    parsed_data = parser.parse_file(filename)
    method = json.loads(parsed_data)[method_id]
    params = method.get('params')
    preconditions = method.get('preconditions')
    loops = method.get('loops')
    return params, preconditions, loops

def parse_params(params):
    parsed_params = []
    for param in params:
        param = param.get('name')
        param = z3Real(f'{param}')
        parsed_params.append(param)

    return parsed_params

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

def set_basis_and_matrix(vars_sym, vars_init, vars_trans, params, degree):

    b_v = sorted(list(itermonomials(vars_sym, degree)), 
                   key=lambda m: (total_degree(m), str(m)))
    
    apply_basis = lambdify(vars_sym, b_v, 'numpy')
    b_v_init = apply_basis(*vars_init)
    b_v_init_const = apply_basis(*vars_init)

    M = []
    for ele in b_v:
        expr = ele.subs(list(zip(vars_sym, vars_trans)))
        transition = [int(Poly(expr, *vars_sym).coeff_monomial(mono)) for mono in b_v]
        M.append(transition)
    M = np.array(M)

    for param in params:
        b_v_init.append(param)
        b_v_init_const.append(0)

        M = np.pad(M, ((0, 1), (0, 1)))
        M[-1, -1] = 1
    
    return b_v_init, b_v_init_const, M
    

def parse_pre_loop(params, preconditions, loop_condition, loop_path):
    params = parse_params(params)
    

def get_transition_matrix():
    pass

def get_loop_guard():
    pass

def get_internal_guard():
    pass