import numpy as np
import copy

class Gauss:
    FLOAT_ACCURACY = 0.00000001

    @staticmethod
    def __direct_walk(matrix: list, free_coefs: list) -> list:
        n_variables = len(matrix)
        matrix = copy.copy(matrix)
        free_coefs = copy.copy(free_coefs)

        for n_step in range(n_variables - 1):
            for n_row in range(n_step + 1, n_variables):
                coef = matrix[n_row][n_step] / matrix[n_step][n_step]
                matrix[n_row] = matrix[n_row] - coef * matrix[n_step]
                free_coefs[n_row] = free_coefs[n_row] - coef * free_coefs[n_step]
        return matrix, free_coefs

    @staticmethod
    def __inverse_walk(matrix: list, free_coefs: list) -> list:
        n_variables = len(matrix)

        answers = np.zeros(n_variables, dtype=float)
        for n_var in range(n_variables)[::-1]:
            var_value = (free_coefs[n_var] - np.dot(answers[n_var + 1:], matrix[n_var][n_var + 1:])) / matrix[n_var][n_var]
            if abs(var_value) < Gauss.FLOAT_ACCURACY:
                var_value = 0
            answers[n_var] = var_value
        return answers

    @staticmethod
    def solve(matrix: np.ndarray, frees: np.ndarray) -> np.ndarray:
        matrix, frees = Gauss.__direct_walk(matrix, frees)
        answers = Gauss.__inverse_walk(matrix, frees)
        return answers

