from types import FunctionType
import numpy as np
import sys
sys.path.insert(1, sys.path[0].split("src")[0] + "src")
from LinearEquationsSystemSolve import Tridiagonal 

def solve(
    p: FunctionType,
    q: FunctionType,
    f: FunctionType,
    alphas: list,
    betas: list,
    a: float,
    b: float,
    h: float) -> tuple:

    x = np.arange(a, b, h)
    n = len(x)
    solve_matrix = np.zeros([n, n])
    solve_frees = np.zeros([n, 1])

    for i in range(n):
        if i == 1:
            __make_first_equation(solve_matrix, solve_frees, alphas, h)
        if i == n - 1:
            __make_last_equation(solve_matrix, solve_frees, betas, h)
        else:
            __make_common_equation(solve_matrix, solve_frees, p, q, f, x, i, h)

    y = Tridiagonal.solve(solve_matrix, solve_frees)
    return x, y

def __make_first_equation(matrix: np.ndarray, frees: np.ndarray, alphas: list, h: float) -> None:
    matrix[0][0] = alphas[0] - alphas[1] / h
    matrix[0][1] = alphas[1] / h
    frees[0] = alphas[2]

def __make_last_equation(matrix: np.ndarray, frees: np.ndarray, betas: list, h: float) -> None:
    n = len(frees) - 1
    matrix[n][n] = betas[0] + betas[1] / h
    matrix[n][n - 1] = -betas[1] / h
    frees[n] = betas[2]

def __make_common_equation(matrix: np.ndarray, frees: np.ndarray, p: FunctionType, q: FunctionType, f: FunctionType, x: list, i: int, h: float):
    k_m1 = 1/h**2 - p(x[i]) / 2*h
    k = -2/h**2 + q(x[i])
    k_p1 = 1/h**2 + p(x[i]) / 2*h

    matrix[i][i-1] = k_m1
    matrix[i][i] = k
    matrix[i][i+1] = k_p1
    frees[i] = f(x[i])