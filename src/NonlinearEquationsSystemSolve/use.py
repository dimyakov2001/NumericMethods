import numpy as np
from types import FunctionType
import math
from SimpleIter_Siedel_Newton_ShortNewton import MethodModes, solve

F_matrix = np.array([
    lambda args: (3**0.5) * args[0] - 2*math.sin(args[0]**2) - 3*(2**0.5) * args[1] - 0.5,
    lambda args: args[0]**2 + 2*args[1]**2 - 1
], dtype=FunctionType).reshape([-1, 1])


jacobi_matrix = np.array([
    [lambda args: 3**0.5 - 4*args[0]*math.cos(args[0]**2),    lambda args: -3*2**0.5],
    [lambda args: 2*args[0],                                            lambda args: 4*args[1]]
], dtype=FunctionType)

start_values = [1, -0.7]
e = 0.01

print("ShortNewton (SimpleIter): {}".format(solve(F_matrix, jacobi_matrix, start_values, e, MethodModes.ShortNewton)))
print("Newton: {}".format(solve(F_matrix, jacobi_matrix, start_values, e, MethodModes.Newton)))
print("Siedel: {}".format(solve(F_matrix, jacobi_matrix, start_values, e, MethodModes.Siedel)))
