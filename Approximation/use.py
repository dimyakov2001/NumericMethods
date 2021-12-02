from . import LinearApproximation
from . import ThirdDegreePolinomialApproximation
from . import LinearizationApproximation, LinearizationApproximationFunctionPack
import numpy as np
import pylab as plt
from math import exp, log
from sklearn.metrics import mean_squared_error

def show_approximation(approximation_funcs: dict, x: list, y: list, dots_colours: list=None, figsize: list=(6, 3), resolution: float=100):
    plt.figure(figsize=figsize)
    plot_x = np.linspace(np.min(x), np.max(x), resolution)

    funcs = list(approximation_funcs.keys())

    for func_key in funcs:
        plot_y = list(map(lambda x: approximation_funcs[func_key](x), plot_x))
        plt.plot(plot_x, plot_y, label=func_key, alpha=0.3, lw=3)

    plt.scatter(x, y, c=dots_colours)
    plt.legend()
    plt.show()


x = np.array([-1, 1, 2, 3], dtype=float)
y = np.array([5, 3, 7, 11], dtype=float)

linear_approximation = LinearApproximation.make_approximation(x, y)
polinomial_approximation = ThirdDegreePolinomialApproximation.make_approximation(x, y)

linearization_approximation_functions = LinearizationApproximationFunctionPack()
linearization_approximation_functions.x = lambda x, y: x*y
linearization_approximation_functions.y = lambda x, y: y
linearization_approximation_functions.A = lambda A, B: -B/A
linearization_approximation_functions.B = lambda A, B: -1/A
linearization_approximation_functions.result = lambda x, a, b: a / (x + b)

linearization_approximation = LinearizationApproximation.make_approximation(x, y, linearization_approximation_functions)

show_approximation(
    {
        "Linear": linear_approximation,
        "3rd degree Polinomial": polinomial_approximation,
        "Linearization": linearization_approximation
    }, x, y
)

y_pred = np.array(list(map(lambda x: linearization_approximation(x), x)))
print("Ошибка аппроксимации произвольной функцией: {}".format(mean_squared_error(y_pred=y_pred, y_true=y)**0.5))



x = np.array([-1, 1, 2, 4], dtype=float)
y = np.array([4, 0, -2, -6], dtype=float)
linear_approximation = LinearApproximation.make_approximation(x, y)
polinomial_approximation = ThirdDegreePolinomialApproximation.make_approximation(x, y)
show_approximation(
    {
        "Linear": linear_approximation,
        "3rd degree Polinomial": polinomial_approximation
    }, x, y
)

x = np.array([1.5, 2.5, 3.3, 4], dtype=float)
y = np.array([9, 31, 66, 108], dtype=float)

