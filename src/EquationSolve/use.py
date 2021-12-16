from Bisection import solve as bisection_solve
from Newton import solve as newton_solve
from SimpleIteration import solve as simpleIter_solve

def f(x: float) -> float:
    return x**3 + 7*x - 3

def df_dx(x: float) -> float:
    return 3*(x**2) + 7

def d2f_dx2(x:float) -> float:
    return 6*x

a = -1
b = 2
e = 0.01

print("Bisection: {}".format(bisection_solve(f, a, b, e)))
print("Newton: {}".format(newton_solve(f, df_dx, d2f_dx2, a, b, e)))
print("Simple iter: {}".format(simpleIter_solve(f, df_dx, a, e)))
