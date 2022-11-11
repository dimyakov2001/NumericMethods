import numpy as np
from enum import Enum
from types import FunctionType

from numpy.core.fromnumeric import mean

INTEGRATION_METHOD_LEFT = "left"
INTEGRATION_METHOD_RIGHT = "right"
INTEGRATION_METHOD_CENTRAL = "center"
INTEGRATION_METHOD_TRAPEZOID = "trapezoid"
INTEGRATION_METHOD_PARABOLA = "parabola"


def calculate(function: FunctionType, start: float, stop: float, intervals: float, method: str):
    x = np.linspace(start, stop, intervals + 1)

    if method == INTEGRATION_METHOD_PARABOLA:
        x = np.linspace(start, stop, 2*intervals + 1)

    sum = 0
    for i in range(intervals):
        sum += __calculate_rectangle_quadrature(function, x, i, method)

    return sum

def __calculate_rectangle_quadrature(function: FunctionType, x: list, i: int, method: str):
    if method == INTEGRATION_METHOD_LEFT:
        return __calculate_left_rectange_quadrature(function, x[i], x[i+1])

    if method == INTEGRATION_METHOD_RIGHT:
        return __calculate_right_rectange_quadrature(function, x[i], x[i+1])

    if method == INTEGRATION_METHOD_CENTRAL:
        return __calculate_center_rectange_quadrature(function, x[i], x[i+1])

    if method == INTEGRATION_METHOD_TRAPEZOID:
        return __calculate_trapezoid_quadrature(function, x[i], x[i+1])

    if method == INTEGRATION_METHOD_PARABOLA:
        return __calculate_parabola_quadrature(function, x[2*i], x[2*i + 1], x[2*i + 2])

def __calculate_left_rectange_quadrature(function: FunctionType, left_value: float, right_value: float):
    h = np.abs(right_value - left_value)
    f = function(left_value)
    return h * f

def __calculate_right_rectange_quadrature(function: FunctionType, left_value: float, right_value: float):
    h = np.abs(right_value - left_value)
    f = function(right_value)
    return h * f

def __calculate_center_rectange_quadrature(function: FunctionType, left_value: float, right_value: float):
    h = np.abs(right_value - left_value)
    center = (right_value + left_value) / 2
    f = function(center)
    return h * f

def __calculate_trapezoid_quadrature(function: FunctionType, left_value: float, right_value: float):
    return (function(left_value) + function(right_value)) * (right_value - left_value) / 2

def __calculate_parabola_quadrature(function: FunctionType, left_value: float, middle_value: float, right_value: float):
    return (function(left_value) + 4*function(middle_value) + function(right_value)) * (right_value - left_value) / 6