from . import DifferentialEquation, DifferentialEquationSolveMethol
from . import BoundaryValueProblem

def derivative(x, y):
    return -8 + 2*x - y

x_start = 1
x_end = 3
y_start = 3
h = 0.4

x, y = DifferentialEquation.solve(derivative, x_start, x_end, y_start, h, DifferentialEquationSolveMethol.Euler)
print("Решение ДУ методом Эйлера:")
print("x: ", x)
print("y: ", y)

x, y = DifferentialEquation.solve(derivative, x_start, x_end, y_start, h, DifferentialEquationSolveMethol.ModifiedEuler)
print("Решение ДУ модифицированным методом Эйлера:")
print("x: ", x)
print("y: ", y)

x, y = DifferentialEquation.solve(derivative, x_start, x_end, y_start, h, DifferentialEquationSolveMethol.RungeKutt)
print("Решение ДУ методом Рунге-Кутта:")
print("x: ", x)
print("y: ", y)


def p(x):
    return -x

def q(x):
    return 2

def f(x):
    return x + 1

a = 0.9
b = 1.2
h = 0.1
alphas = [0, 1, 2]
betas = [0, 1, 1]
x, y = BoundaryValueProblem.solve(p, q, f, alphas, betas, a, b, h)
print("Решение кравевой задачи для линейного ДУ второго порядка:")
print("x: ", x)
print("y: ", y)