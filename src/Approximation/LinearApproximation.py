from types import FunctionType
import numpy as np
import sys
sys.path.insert(1, sys.path[0].split("src")[0] + "src")
from LinearEquationsSystemSolve import Gauss

def make_approximation(x: np.ndarray, y: np.ndarray) -> FunctionType:
    matrix = __make_matrix(x)
    frees = __make_free_coefs_vector(x, y)

    a, b = Gauss.solve(matrix, frees)
    
    return lambda x: a*x + b

def __make_matrix(x: np.ndarray) -> np.ndarray:
    return np.array(
        [[np.sum(x**2), np.sum(x)],
        [np.sum(x), len(x)]],
        dtype=float
    )

def __make_free_coefs_vector(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.array([np.sum(x * y), np.sum(y)], dtype=float)
