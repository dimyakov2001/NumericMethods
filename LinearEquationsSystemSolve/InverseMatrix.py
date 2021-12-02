import numpy as np

FLOAT_ACCURACY = 0.00000001

class InverseMatrix:
    @staticmethod
    def solve(matrix: np.ndarray, frees: np.ndarray) -> np.ndarray:
        invert_matrix = np.linalg.inv(matrix)
        answers = np.dot(invert_matrix, frees)
        answers = list(map(lambda x: x if abs(x) >= FLOAT_ACCURACY else 0, answers))
        return answers
