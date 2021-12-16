from Integration import Integration, IntegrationMethods

def function(x):
    return 3*x**2 + 5 + x**0.5

n = 6
start = 0
stop = 3

print("Метод левых прямоугольников: {}".format(
    Integration.calculate(function, start, stop, n, IntegrationMethods.Left)
))
print("Метод правых прямоугольников: {}".format(
    Integration.calculate(function, start, stop, n, IntegrationMethods.Right)
))
print("Метод центральных прямоугольников: {}".format(
    Integration.calculate(function, start, stop, n, IntegrationMethods.Central)
))
print("Метод трапеций: {}".format(
    Integration.calculate(function, start, stop, n, IntegrationMethods.Trapezoid)
))
print("Метод парабол: {}".format(
    Integration.calculate(function, start, stop, n, IntegrationMethods.Parabola)
))
