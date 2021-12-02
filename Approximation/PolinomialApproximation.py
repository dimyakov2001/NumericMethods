from types import FunctionType
import numpy as np
from NonlinearEquationsSystemSolve import NonLinearEquationSystemSolve, MethodModes


class ThirdDegreePolinomialApproximation:
    system_slove_start_values = [1, 1, 1]
    system_slove_accuracy = 0.001
    system_solve_method = MethodModes.ShortNewton


    @staticmethod
    def make_approximation(x: np.ndarray, y: np.ndarray, ) -> FunctionType:
        F_matrix = ThirdDegreePolinomialApproximation.__make_F_matrix(x, y)
        jacobi_matrix = ThirdDegreePolinomialApproximation.__make_jacobi_matrix(x)

        a, b, c = NonLinearEquationSystemSolve.solve(
            F_matrix,
            jacobi_matrix,
            ThirdDegreePolinomialApproximation.system_slove_start_values,
            ThirdDegreePolinomialApproximation.system_slove_accuracy,
            ThirdDegreePolinomialApproximation.system_solve_method
        )
        
        return lambda x: a*x**2 + b*x + c

    @staticmethod
    def __make_F_matrix(x: np.ndarray, y: np.ndarray) -> np.ndarray:
        return np.array(
           [lambda args: args[0]*np.sum(x**4) + args[1]*np.sum(x**3) + args[2]*np.sum(x**2) - np.sum(y*(x**2)),
            lambda args: args[0]*np.sum(x**3) + args[1]*np.sum(x**2) + args[2]*np.sum(x) - np.sum(y*x),
            lambda args: args[0]*np.sum(x**2) + args[1]*np.sum(x) + args[2]*len(x) - np.sum(y)
            ],
            dtype=FunctionType
        ).reshape([-1, 1])

    @staticmethod
    def __make_jacobi_matrix(x: np.ndarray) -> np.ndarray:
        return np.array(
            [[lambda args: np.sum(x**4), lambda args: np.sum(x**3), lambda args: np.sum(x**2)],
             [lambda args: np.sum(x**3), lambda args: np.sum(x**2), lambda args: np.sum(x)],
             [lambda args: np.sum(x**2), lambda args: np.sum(x),    lambda args: len(x)],
            ],
            dtype=FunctionType
        )
