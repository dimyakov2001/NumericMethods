from types import FunctionType
import numpy as np
from LinearEquationsSystemSolve import Gauss


class LinearizationApproximationFunctionPack:
    x = None
    y = None
    A = None
    B = None
    result = None

    def __init__(self) -> None:
        self.x = None
        self.y = None
        self.A = None
        self.B = None
        self.result = None


def make_approximation(x: np.ndarray, y: np.ndarray, functions: LinearizationApproximationFunctionPack) -> FunctionType:

    X = __linearize_xy(x, y, functions.x)
    Y = __linearize_xy(x, y, functions.y)

    matrix = __make_matrix(X)
    frees = __make_free_coefs_vector(X, Y)

    A, B = Gauss.solve(matrix, frees)

    a = __delinearize_AB(A, B, functions.A)
    b = __delinearize_AB(A, B, functions.B)
    
    return lambda x: functions.result(x, a, b)

def __linearize_xy(x: np.ndarray, y: np.ndarray, linearization_func: FunctionType):
    return np.array(list(map(
        lambda i: linearization_func(x[i], y[i]),
        range(len(x))
    )))

def __make_matrix(x: np.ndarray) -> np.ndarray:
    return np.array(
        [[np.sum(x**2), np.sum(x)],
        [np.sum(x), len(x)]],
        dtype=float
    )

def __make_free_coefs_vector(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.array([np.sum(x * y), np.sum(y)], dtype=float)

def __delinearize_AB(A: float, B: float, delinearization_function: FunctionType) -> float:
    return delinearization_function(A, B)


