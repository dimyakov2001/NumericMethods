from DifferrentialEquation import DifferentialEquation, DifferentialEquationSolveMethol

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