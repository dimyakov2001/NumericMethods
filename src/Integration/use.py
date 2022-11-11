import Integration

def function(x):
    return 3*x**2 + 5 + x**0.5

n = 6
start = 0
stop = 3

print("Метод левых прямоугольников: {}".format(
    Integration.calculate(function, start, stop, n, Integration.INTEGRATION_METHOD_LEFT)
))
print("Метод правых прямоугольников: {}".format(
    Integration.calculate(function, start, stop, n, Integration.INTEGRATION_METHOD_RIGHT)
))
print("Метод центральных прямоугольников: {}".format(
    Integration.calculate(function, start, stop, n, Integration.INTEGRATION_METHOD_CENTRAL)
))
print("Метод трапеций: {}".format(
    Integration.calculate(function, start, stop, n, Integration.INTEGRATION_METHOD_TRAPEZOID)
))
print("Метод парабол: {}".format(
    Integration.calculate(function, start, stop, n, Integration.INTEGRATION_METHOD_PARABOLA)
))
