import functools
from . import Integration

bounds = [(0, 1), (1, 2), (0, 3)]
n = 100

def function(args):
    return 3*args[0] + args[1] + args[2]

print("Вычисление тройного интеграла методом Монте-карло: {}".format(Integration.calculate(bounds, function, n)))
