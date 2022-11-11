import numpy as np
from types import FunctionType
from enum import Enum

class SolveMethod(Enum):
    Euler = "euler"
    ModifiedEuler = "modifiedEuler"
    RungeKutt = "runge-kutt"



def solve(derivative: FunctionType, x_start: float, x_end: float, y_start: float, h: float, method: SolveMethod) -> float:
    x = x_start + h
    x_list = [x_start]
    y_list = [y_start]

    while x < x_end:
        y = __next_value(derivative, x_list[-1], y_list[-1], h, method)
        x_list.append(x)
        y_list.append(y)
        x += h

    return x_list, y_list
    

def __next_value(derivative: FunctionType, x_prev: float, y_prev: float, h: float, method: SolveMethod) -> float:
    if method.value == SolveMethod.Euler.value:
        return __next_value_euler(derivative, x_prev, y_prev, h)
    if method.value == SolveMethod.ModifiedEuler.value:
        return __next_value_modified_euler(derivative, x_prev, y_prev, h)
    if method.value == SolveMethod.RungeKutt.value:
        return __next_value_runge_kutt(derivative, x_prev, y_prev, h)

def __next_value_euler(derivative: FunctionType, x_prev: float, y_prev: float, h: float) -> float:
    return y_prev + h * derivative(x_prev, y_prev)

def __next_value_modified_euler(derivative: FunctionType, x_prev: float, y_prev: float, h: float) -> float:
    y_ = __next_value_euler(derivative, x_prev, y_prev, h)
    x_ = x_prev + h
    return y_prev + (derivative(x_prev, y_prev) + derivative(x_, y_)) * h / 2

def __next_value_runge_kutt(derivative: FunctionType, x_prev: float, y_prev: float, h: float) -> float:
    k0 = h * derivative(x_prev, y_prev)
    k1 = h * derivative(x_prev + h/2, y_prev + k0/2)
    k2 = h * derivative(x_prev + h/2, y_prev + k1/2)
    k3 = h * derivative(x_prev + h, y_prev + k2)
    return y_prev + (k0 + 2*k1 + 2*k2 + k3)/6

    
