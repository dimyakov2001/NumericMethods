import functools
import numpy as np
from . import Integration
from . import LinearSystem

bounds = [(0, 1), (1, 2), (0, 3)]
n = 10000

def function(args):
    return 3*args[0] + args[1] + args[2]

print("Вычисление тройного интеграла методом Монте-карло: {}".format(Integration.calculate(bounds, function, n)))

a = np.array([[0.4, 0.1], [0.1, 0.5]])
f = np.array([0.3, 0.3])

n = 100
e = 0.01

print("Решение СЛАУ методом Монте-карло: {}".format(LinearSystem.solve(a, f, n, e)))

