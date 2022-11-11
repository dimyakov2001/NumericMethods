import numpy as np
import copy

    
def __metod_converges(matrix: list) -> bool:
    metod_converge_val = True
    i = 0
    while metod_converge_val and i < len(matrix):
        row = list(np.abs(matrix[i]))
        row_diag_elem = row.pop(i)
        if sum(row) > row_diag_elem:
            metod_converge_val = False
        i += 1
    return metod_converge_val

def __start_method(matrix: list, free: list, e: float, siedel_method: bool = False) -> list:
    vars = np.zeros(len(matrix), dtype=float)
    stop_flag = False

    while not stop_flag:
        vars_prev = copy.copy(vars)
        for i in range(len(vars)):
            x_first_sum = 0

            if siedel_method:
                x_first_sum = np.dot(vars[:i], matrix[i][:i])
            else:
                x_first_sum = np.dot(vars_prev[:i], matrix[i][:i])

            x_i = (free[i] - x_first_sum - np.dot(vars_prev[i + 1:], matrix[i][i + 1:])) / matrix[i][i]
            vars[i] = x_i
        stop_flag = __need_continue(vars_prev, vars, e)
    return vars

def __need_continue(x_prev: list, x_next: list, e: float) -> bool:
    errors = np.abs(x_prev - x_next)
    max_error = max(errors)
    return max_error < e

def solve(matrix: np.ndarray, frees: np.ndarray, e: float, siedel_method: bool=False) -> np.ndarray:
    if __metod_converges(matrix):
        return __start_method(matrix, frees, e, siedel_method=siedel_method)
    else:
        return None



