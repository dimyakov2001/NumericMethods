import numpy as np
import Gauss
import GaussWithError
import InverseMatrix
import SimpleIter_Siedel
import SimpleIter_SiedelWithCheck
import Tridiagonal

# Inverse
matrix = np.array(
       [[5, 1,  1, 2],
        [2, 4,  1, 2],
        [1, 1,  3, 1],
        [1, 1, -1, 3]], dtype=float)
frees = np.array([2, 5, 4, 0], dtype=float)

print("Inverse: {}".format(InverseMatrix.solve(matrix, frees)))

# Gauss
matrix = np.array(
         [[6.63, 11.75,  10.0],
          [7.42, 19.03,  11.75],
          [5.77, 7.48,  6.36]], dtype=float)
frees = np.array([-41.4, -49.49, -27.67], dtype=float)

print("Simple Gauss: {}".format(Gauss.solve(matrix, frees)))
print("Gauss with error count: {}".format(GaussWithError.solve(matrix, frees)))

# Tridiag
matrix = np.array(
       [[-10, 4,  0, 0],
        [1, 2,  -0.2, 0],
        [0, -1,  7, -1],
        [0, 0, 2, -5]], dtype=float)
frees = np.array([-8, 5.5, -2, 1], dtype=float)

print("Tridiagonal: {}".format(Tridiagonal.solve(matrix, frees)))

# SimpleIter - Siedel
# SimpleIter - Siedel with convergence check
matrix = np.array(
       [[3, 1,  -1],
        [1, -4,  1],
        [-1, 1,  4]], dtype=float)
frees = np.array([0.5, -2.1, -0.3], dtype=float)
e = 0.0001

print("Simple Iter: {}".format(SimpleIter_Siedel.solve(matrix, frees, e)))
print("Siedel: {}".format(SimpleIter_Siedel.solve(matrix, frees, e, siedel_method=True)))
print("Simple Iter with convergence check: {}".format(SimpleIter_SiedelWithCheck.solve(matrix, frees, e)))
print("Siedel with convergence check: {}".format(SimpleIter_SiedelWithCheck.solve(matrix, frees, e, siedel_method=True)))
