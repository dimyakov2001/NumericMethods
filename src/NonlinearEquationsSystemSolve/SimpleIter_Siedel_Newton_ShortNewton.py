import numpy as np
from enum import Enum
from copy import copy


METHOD_SHORT_NEWTON = "short Newton"
METHOD_SIEDEL = "siedel"
METHOD_NEWTON = "Newton"

# ------ Проверка на сходимость ------- #

def __method_converges(jacobi_matrix, start_values):
    jacobi_matrix_values_in_start = __matrix_in_point(jacobi_matrix, start_values)
    jacoby_in_start_det = np.linalg.det(jacobi_matrix_values_in_start)
    return jacoby_in_start_det

def __matrix_in_point(functions_matrix, args):
    args = np.array(args, dtype=float)
    values_matrix =  np.zeros(functions_matrix.shape)
    for n_row in range(functions_matrix.shape[0]):
        for n_col in range(functions_matrix.shape[1]):
            values_matrix[n_row][n_col] = functions_matrix[n_row][n_col](args)

    return values_matrix

# ------ Основной ход метода -------- #

def __start_method(F_matrix, jacobi_matrix, start_values, e, mode: str):
    x_i = np.array(start_values, dtype=float).reshape([-1, 1])
    stop_flag = False
    n_iter = 0
    lambd_matrix = [[]]

    if mode != METHOD_NEWTON:
        lambd_matrix = __calculate_lambd_matrix(jacobi_matrix, x_i)

    while not stop_flag:
        if mode == METHOD_NEWTON:
            lambd_matrix = __calculate_lambd_matrix(jacobi_matrix, x_i)

        if mode == METHOD_SIEDEL:
            x_i_plus_one = __siedel_method_step(F_matrix, lambd_matrix, x_i)
        else:
            F_in_x_i = __matrix_in_point(F_matrix, x_i)
            delta_x = np.dot(lambd_matrix, F_in_x_i)
            x_i_plus_one = x_i + delta_x

        stop_flag = __may_stop(x_i, x_i_plus_one, e)
        x_i = x_i_plus_one
        n_iter += 1
    
    return x_i

def __calculate_lambd_matrix(jacoby_matrix, x_i):
    jacobian_in_x_i = __matrix_in_point(jacoby_matrix, x_i)
    inverse_jacobian_in_x_i = np.linalg.inv(jacobian_in_x_i)
    negative_inverse_jacobian_in_x_i = -inverse_jacobian_in_x_i
    return negative_inverse_jacobian_in_x_i

def __siedel_method_step(F_matrix, lambd_matrix, x_i):
    x_i_plus_one = copy(x_i)
    for n_row in range(len(F_matrix)):
        x_i_plus_one[n_row] = x_i[n_row] + np.dot(lambd_matrix[n_row], __matrix_in_point(F_matrix, x_i_plus_one))
    return x_i_plus_one

def __may_stop(x_i, x_i_plus_one, e):
    return np.max(np.abs(x_i - x_i_plus_one)) < e

# ------- Запуск -------- #

def solve(F_matrix: np.ndarray, jacobi_matrix: np.ndarray, start_values: list, e: float, method: str):
    jacobi_in_start_det = __method_converges(jacobi_matrix, start_values)
    if jacobi_in_start_det != 0:
        ans = __start_method(F_matrix, jacobi_matrix,  start_values, e, method)
        return np.transpose(ans)[0]
    else:
        return None

