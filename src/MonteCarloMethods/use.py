import numpy as np
from . import Integration
from . import LinearSystem
from . import FigureArea

bounds = [(0, 1), (1, 2), (0, 3)]
n = 10000

def function(args):
    return 3*args[0] + args[1] + args[2]

print("Вычисление тройного интеграла методом Монте-Карло: {}".format(Integration.calculate(bounds, function, n)))

a = np.array([[0.4, 0.1], [0.1, 0.5]])
f = np.array([0.3, 0.3])

n = 100
e = 0.01

print("Решение СЛАУ методом Монте-Карло: {}".format(LinearSystem.solve(a, f, n, e)))


borders = [
    lambda point: -point[0]**3 + point[1]**5 < 2,
    lambda point: point[0] - point[1] < 1
]
base_square = np.array([[-2, 2], [2, -2]])
n_points = 10000

print("Вычисление площади фигуры методом Монте-Карло: {}".format(FigureArea.calculate(base_square, borders, n_points)))
