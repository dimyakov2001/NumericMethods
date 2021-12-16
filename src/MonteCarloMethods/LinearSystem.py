import numpy as np
from functools import reduce
from copy import copy

class LinearSystem:
    __coefs = []
    __frees = []
    __n = 0
    __e = 100.0

    @staticmethod
    def solve(coefs: np.ndarray, frees: np.ndarray, n: int, e: float) -> np.ndarray:
        """
        Решение СЛАУ вида x_i = a_i1 * x_1 + ... + a_ij * x_j + ... + a_in * x_n + b_i

        Args:
            coefs – матрица a_ij
            frees – вектор b_i
            n – число розыгрышей при вычислении X_i на m-ом шаге
            e – точность (критерий остановки)

        Returns:
            Вектор с x_i
        """
        LinearSystem.__coefs = coefs
        LinearSystem.__frees = frees
        LinearSystem.__n = n
        LinearSystem.__e = e
        p_coefs = LinearSystem.__make_p_coefs(coefs)

        may_stop = False
        prev_c_means = frees
        c_means = frees

        while not may_stop:
            prev_c_means = c_means
            c_means = LinearSystem.__make_step(c_means, p_coefs)
            may_stop = LinearSystem.__may_stop(prev_c_means, c_means)

        return c_means


    @staticmethod
    def __make_p_coefs(coefs: np.ndarray) -> np.ndarray:
        coefs_abs = np.abs(coefs)
        coefs_rows_sum = np.sum(coefs_abs, axis=1).reshape(-1, 1)
        coefs_normalize_dividers = np.repeat(coefs_rows_sum, coefs.shape[1], axis=1)
        p_coefs = coefs_abs / coefs_normalize_dividers
        return p_coefs


    @staticmethod
    def __make_step(c_means: np.ndarray, p_coefs: np.ndarray):
        c_means = copy(c_means)
        n_vars = len(c_means)
        for step in range(n_vars):
            c_means[step] = LinearSystem.__get_mean_c(step, c_means, p_coefs)
        return c_means


    @staticmethod
    def __get_mean_c(step_in_iter: int, c_means: np.ndarray, p_coefs: np.ndarray):
        c_sum = reduce(lambda summ, _: summ + LinearSystem.__get_random_c(step_in_iter, c_means, p_coefs), np.arange(0, LinearSystem.__n), 0)
        c_mean = c_sum / LinearSystem.__n
        return c_mean


    @staticmethod
    def __get_random_c(step_in_iter: int, c_means: np.ndarray, p_coefs: np.ndarray):
        random_index = LinearSystem.__get_random_index(p_coefs[step_in_iter])
        f_i = LinearSystem.__frees[step_in_iter]
        c_mean_j = c_means[random_index]
        a_ij = LinearSystem.__coefs[step_in_iter][random_index]
        p_ij = p_coefs[step_in_iter][random_index]
        random_c = f_i + c_mean_j * a_ij / p_ij
        return random_c


    @staticmethod
    def __get_random_index(p_coefs: list) -> int:
        index_list = np.arange(0, len(p_coefs), dtype=int)
        random_index = np.random.choice(index_list, p=p_coefs)
        return random_index


    @staticmethod
    def __may_stop(prev_c: np.ndarray, curr_c: np.ndarray) -> bool:
        devitations = np.abs(prev_c - curr_c)
        return np.max(devitations) < LinearSystem.__e