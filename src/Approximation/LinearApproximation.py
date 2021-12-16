from types import FunctionType
import numpy as np
from LinearEquationsSystemSolve import Gauss


class LinearApproximation:

    @staticmethod
    def make_approximation(x: np.ndarray, y: np.ndarray) -> FunctionType:
        matrix = LinearApproximation.__make_matrix(x)
        frees = LinearApproximation.__make_free_coefs_vector(x, y)

        a, b = Gauss.solve(matrix, frees)
        
        return lambda x: a*x + b

    @staticmethod
    def __make_matrix(x: np.ndarray) -> np.ndarray:
        return np.array(
           [[np.sum(x**2), np.sum(x)],
            [np.sum(x), len(x)]],
            dtype=float
        )

    @staticmethod
    def __make_free_coefs_vector(x: np.ndarray, y: np.ndarray) -> np.ndarray:
        return np.array([np.sum(x * y), np.sum(y)], dtype=float)
