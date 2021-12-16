from types import FunctionType
import numpy as np
import copy


class SimpleIter_SiedelWithConvergenceCheck:
    FLOAT_ACCURACY = 0.00000001

    def __to_normal_form(matrix: list, frees: list) -> list:
        normal_form_matrix = []
        normal_form_frees = []
        for n_equation in range(len(matrix)):
            normal_equation = np.hstack([
                -matrix[n_equation][:n_equation],
                [0.0],
                -matrix[n_equation][n_equation + 1:],
                frees[n_equation]
            ])
            normal_equation /= matrix[n_equation][n_equation]
            normal_form_matrix.append(normal_equation[:-1])
            normal_form_frees.append(normal_equation[-1])
        return np.array(normal_form_matrix), np.array(normal_form_frees)


    def __get_alpha(matrix: list) -> list:

        alpha = SimpleIter_SiedelWithConvergenceCheck.__calculate_alhpa_1(matrix)
        if alpha < 1.0:
            return alpha, SimpleIter_SiedelWithConvergenceCheck.__calculate_rho_1

        alpha = SimpleIter_SiedelWithConvergenceCheck.__calculate_alhpa_2(matrix)
        if alpha < 1.0:
            return alpha, SimpleIter_SiedelWithConvergenceCheck.__calculate_rho_2

        alpha = SimpleIter_SiedelWithConvergenceCheck.__calculate_alhpa_3(matrix)
        if alpha < 1.0:
            return alpha, SimpleIter_SiedelWithConvergenceCheck.__calculate_rho_3

        return 0, None

    def __calculate_rho_1(x, y):
        abs_list = list(map(lambda i: np.abs(x[i] - y[i]), range(len(x))))
        return np.max(abs_list)

    def __calculate_alhpa_1(matrix: list) -> bool:
        row_sums = list(map(lambda row: np.sum(np.abs(row)), matrix))
        return np.max(row_sums)

    def __calculate_rho_2(x, y):
        return np.sum(np.abs(x - y))

    def __calculate_alhpa_2(matrix: list) -> bool:
        row_sums = list(map(lambda row: np.sum(np.abs(row)), np.transpose(matrix)))
        return np.max(row_sums)

    def __calculate_rho_3(x, y):
        return np.sum((x - y) ** 2) ** 0.5

    def __calculate_alhpa_3(matrix: list) -> bool:
        return np.sum(matrix ** 2)

    def __start_method(matrix: list, free: list, e: float, alpha: float, rho_func: FunctionType, siedel_method: bool = False) -> list:
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

                x_second_sum = np.dot(vars_prev[i + 1:], matrix[i][i + 1:])

                x_i = (free[i] + x_first_sum + x_second_sum)
                vars[i] = x_i
            stop_flag = SimpleIter_SiedelWithConvergenceCheck.__need_continue(vars_prev, vars, e, alpha, rho_func)
        return vars


    def __need_continue(x_prev: list, x_next: list, e: float, alpha: float, rho_func: FunctionType) -> bool:
        return rho_func(x_prev, x_next) <= e * (1 - alpha) / alpha


    def solve(matrix: np.ndarray, frees: np.ndarray, e: float, siedel_method: bool=False) -> np.ndarray:
        normal_matrix, normal_frees = SimpleIter_SiedelWithConvergenceCheck.__to_normal_form(matrix, frees)
        alpha, rho_func = SimpleIter_SiedelWithConvergenceCheck.__get_alpha(normal_matrix)
        if np.abs(alpha) > SimpleIter_SiedelWithConvergenceCheck.FLOAT_ACCURACY:
            return SimpleIter_SiedelWithConvergenceCheck.__start_method(normal_matrix, normal_frees, e, alpha, rho_func, siedel_method)
        else:
            return None

