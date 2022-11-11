import numpy as np
import copy
from Float import Float

FLOAT_ACCURACY = 0.00000001

def __direct_walk(matrix: list, free_coefs: list) -> list:
    n_variables = len(matrix)
    matrix = copy.copy(matrix)
    free_coefs = copy.copy(free_coefs)

    for n_step in range(n_variables - 1):
        for n_row in range(n_step + 1, n_variables):
            coef = matrix[n_row][n_step].__div__(matrix[n_step][n_step])
            matrix[n_row] = __sub_lists(matrix[n_row], __multiple_float_array_on_float(matrix[n_step], coef))
            free_coefs[n_row] = free_coefs[n_row] - coef * free_coefs[n_step]
    
    return matrix, free_coefs

def __multiple_float_array_on_float(array: list, coef: float) -> list:
    array = copy.copy(array)
    for i in range(len(array)):
        array[i] = coef * array[i]
    return array

def __sub_lists(list1: list, list2: list) -> list:
    new_list = []
    if len(list1) != len(list2):
        raise IndexError("Lists with different dimensions can't be subtracted.")

    for i in range(len(list1)):
        new_list.append(list1[i] - list2[i])
    return new_list

def __inverse_walk(matrix: list, free_coefs: list) -> list:
    n_variables = len(matrix)

    answers = []
    for _ in range(n_variables):
        answers.append(Float(0.0))

    for n_var in range(n_variables)[::-1]:
        var_value = (free_coefs[n_var] - np.dot(answers[n_var + 1:], matrix[n_var][n_var + 1:])).__div__(matrix[n_var][n_var])
        if abs(var_value) < FLOAT_ACCURACY:
            var_value = Float(0.0)
        answers[n_var] = var_value
    return answers

def __make_matrix_floats(matrix: list) -> list:
    matrix = copy.copy(matrix)
    for n_row in range(len(matrix)):
        for n_column in range(len(matrix[n_row])):
            matrix[n_row][n_column] = Float(matrix[n_row][n_column])
    return np.array(matrix)

def __make_frees_floats(free: list) -> list:
    free = copy.copy(free)
    for n_elem in range(len(free)):
        free[n_elem] = Float(free[n_elem])
    return np.array(free)

def __round_answers(answers: list) -> list:
    new_answers = []
    for answer in answers:
        new_answers.append(answer.round_to_error())
    return new_answers

def solve(matrix: np.ndarray, frees: np.ndarray) -> np.ndarray:
    matrix = __make_matrix_floats(matrix.tolist())
    frees = __make_frees_floats(frees.tolist())
    matrix, frees = __direct_walk(matrix, frees)
    answers = __inverse_walk(matrix, frees)
    answers = __round_answers(answers)
    return answers

