import numpy as np


FLOAT_ACCURACY = 0.00000001
NON_ZERO_MATRIX_COEFS_ROW_LEN = 3

def __make_matrix_coefs(matrix: list, free_coefs: list) -> list:
    matrix_coefs = []
    for n_row in range(len(matrix)):
        matrix_coefs_row = []
        index_of_matrix_elem_to_add = n_row - 1

        if n_row == 0:
            matrix_coefs_row.append(0)
            index_of_matrix_elem_to_add = 0
        
        while len(matrix_coefs_row) < NON_ZERO_MATRIX_COEFS_ROW_LEN and index_of_matrix_elem_to_add < len(matrix[n_row]):
            matrix_coefs_row.append(matrix[n_row][index_of_matrix_elem_to_add])
            index_of_matrix_elem_to_add += 1
        
        while len(matrix_coefs_row) < NON_ZERO_MATRIX_COEFS_ROW_LEN:
            matrix_coefs_row.append(0)
        
        matrix_coefs.append(matrix_coefs_row)
    
    matrix_coefs = np.array(matrix_coefs)
    free_coefs = np.array(free_coefs).reshape(-1, 1)
    matrix_coefs = np.hstack([matrix_coefs, free_coefs])
    return matrix_coefs

def __make_uv_matrix(matrix_coefs: list) -> list:
    uv_matrix = np.zeros([len(matrix_coefs) + 1, 2])
    for i in range(1, len(uv_matrix)):
        a_i = matrix_coefs[i - 1][0]
        b_i = matrix_coefs[i - 1][1]
        c_i = matrix_coefs[i - 1][2]
        d_i = matrix_coefs[i - 1][3]
        
        u_i = -c_i/(a_i * uv_matrix[i-1][0] + b_i)
        v_i = (d_i - a_i * uv_matrix[i-1][1]) / (a_i * uv_matrix[i-1][0] + b_i)
        uv_matrix[i][0] = u_i
        uv_matrix[i][1] = v_i
    uv_matrix = np.delete(uv_matrix, 0, axis=0)
    return uv_matrix

def __make_answers(uv_matrix: list) -> list:
    answers = np.zeros(len(uv_matrix) + 1)
    for i in range(len(answers) - 1)[::-1]:
        u = uv_matrix[i][0]
        v = uv_matrix[i][1]
        answers[i] = u * answers[i + 1] + v
    answers = np.delete(answers, -1)
    return answers


def solve(matrix: np.ndarray, frees: np.ndarray) -> np.ndarray:
    matrix_coefs = __make_matrix_coefs(matrix, frees)
    uv_matrix = __make_uv_matrix(matrix_coefs)
    answers = __make_answers(uv_matrix)
    return answers
