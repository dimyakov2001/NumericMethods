from functools import reduce
import numpy as np
from types import FunctionType

import sys
sys.path.insert(1, sys.path[0].split("src")[0] + "src")
from LinearEquationsSystemSolve import Tridiagonal


def make_interpolation(x: list, y: list) -> FunctionType:
    a = __find_a_coefs(y)
    c = __find_c_coefs(x, y)
    b = __find_b_coefs(x, y, c)
    d = __find_d_coefs(x, c)

    splines = __make_splines(x, a, b, c, d)
    return __combine_splines(x, splines)

def __find_a_coefs(y: list) -> list:
    return y[:-1]

def __find_c_coefs(x: list, y: list) -> list:
    matrix = __make_tridiagonal_matrix(x)
    frees = __make_free_coefs_vector(x, y)
    c = Tridiagonal.solve(matrix, frees)
    return c

def __make_tridiagonal_matrix(x: list) -> np.ndarray:
    matrix = np.zeros([len(x), len(x)], dtype=float)
    matrix[0][0] = 1

    for i in range(1, matrix.shape[0] - 1):
        matrix[i][i-1] = x[i] - x[i - 1]
        matrix[i][i] = 2*(x[i + 1] - x[i - 1])
        matrix[i][i+1] = x[i+1] - x[i]

    matrix[matrix.shape[0] - 1][matrix.shape[1] - 1] = 1

    return matrix

def __make_free_coefs_vector(x: list, y: list) -> np.ndarray:
    frees = [0]
    for i in range(2, len(x)):
        frees.append(
            3*((y[i] - y[i-1]) / (x[i] - x[i-1]) - (y[i-1] - y[i-2]) / (x[i-1] - x[i-2]))
        )
    frees.append(0)

    return np.array(frees, dtype=float)
        
def __find_b_coefs(x: list, y: list, c: list) -> list:
    i = 0
    b_list = []
    h_i = 0

    while i < len(c) - 2:
        h_i = x[i+1]- x[i]
        b_list.append(
            (y[i+1] - y[i]) / h_i  - (h_i / 3) * (c[i+1] + 2*c[i])
        )
        i += 1
    
    h_i = x[i+1]- x[i]
    b_list.append(
        (y[i+1] - y[i]) / h_i - (2/3)*h_i*c[i]
    )

    return b_list

def __find_d_coefs(x: list, c: list) -> list:
    i = 0
    d_list = []

    while i < len(c) - 2:
        d_list.append(
            (c[i+1] - c[i]) / (3*(x[i+1] - x[i]))
        )
        i += 1

    d_list.append(
        -c[i] / (3*(x[i+1] - x[i]))
    )

    return d_list

def __make_splines(x: list, a: list, b: list, c: list, d: list) -> list:
    spline_list = list(map(
        lambda i: __make_single_spline(x[i], a[i], b[i], c[i], d[i]),
        range(len(a))
    ))
    return spline_list

def __make_single_spline(x: float, a: float, b: float, c: float, d: float) -> FunctionType:
    return lambda input_x: a + b*(input_x - x) + c*(input_x - x)**2 + d*(input_x - x)**3

def __combine_splines(x: list, splines: list) -> FunctionType:
    return lambda input_x: reduce(
        lambda sum, i: sum + __is_in_interval(input_x, x[i], x[i + 1], (i == len(splines) - 1)) * splines[i](input_x),
        range(len(splines)),
        0
    )

def __is_in_interval(x: float, interval_left: float, interval_right: float, is_end: bool) -> float:
    if is_end:
        return float(interval_left <= x <= interval_right)
    return float(interval_left <= x < interval_right)




