import numpy as np
from numpy.core.defchararray import title
import pylab as plt
from types import FunctionType
from . import LagrangianInterpolation
from . import NewtonInterpolation
from . import SplineInterpolation

def show_interpolation(interpolation_funcs: dict, x: list, y: list, dots_colours: list=None, figsize: list=(6, 3), resolution: float=100):
    plt.figure(figsize=figsize)
    plot_x = np.linspace(np.min(x), np.max(x), resolution)

    funcs = list(interpolation_funcs.keys())

    for func_key in funcs:
        plot_y = list(map(lambda x: interpolation_funcs[func_key](x), plot_x))
        plt.plot(plot_x, plot_y, label=func_key, alpha=0.3, lw=3)

    plt.scatter(x, y, c=dots_colours)
    plt.legend()
    plt.show()


x = np.array([0, 2, 3], dtype=float)
y = np.array([-2, 0, -4], dtype=float)

lagrangian_interpolation_polynomial = LagrangianInterpolation.make_interpolation(x, y)
newton_interpolation = NewtonInterpolation.make_interpolation(x, y)
spline_interpolation = SplineInterpolation.make_interpolation(x, y)
show_interpolation(
    {
        "Lagrangian": lagrangian_interpolation_polynomial,
        "Newton": newton_interpolation,
        "Spline": spline_interpolation
    }, x, y)

x = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0], dtype=float)
y = np.array([0.2, 2.2, 2.6, 2.9, 3.1, 3.2], dtype=float)

spline_interpolation = SplineInterpolation.make_interpolation(x, y)
target_point = 1.1
dots_x = np.hstack([x, [target_point]])
dots_y = np.hstack([y, [spline_interpolation(target_point)]])
dots_colours = np.array(["g"]*len(x) + ["r"])

show_interpolation(
    {
        "Spline": spline_interpolation
    }, dots_x, dots_y, dots_colours)

print(spline_interpolation)
