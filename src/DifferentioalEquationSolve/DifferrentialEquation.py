import numpy as np
from types import FunctionType
from enum import Enum

class DifferentialEquationSolveMethol(Enum):
    Euler = "euler"
    ModifiedEuler = "modifiedEuler"
    RungeKutt = "runge-kutt"


class DifferentialEquation:

    @staticmethod
    def solve(derivative: FunctionType, x_start: float, x_end: float, y_start: float, h: float, method: DifferentialEquationSolveMethol) -> float:
        x = x_start + h
        x_list = [x_start]
        y_list = [y_start]

        while x < x_end:
            y = DifferentialEquation.__next_value(derivative, x_list[-1], y_list[-1], h, method)
            x_list.append(x)
            y_list.append(y)
            x += h

        return x_list, y_list
        

    @staticmethod
    def __next_value(derivative: FunctionType, x_prev: float, y_prev: float, h: float, method: DifferentialEquationSolveMethol) -> float:
        if method.value == DifferentialEquationSolveMethol.Euler.value:
            return DifferentialEquation.__next_value_euler(derivative, x_prev, y_prev, h)
        if method.value == DifferentialEquationSolveMethol.ModifiedEuler.value:
            return DifferentialEquation.__next_value_modified_euler(derivative, x_prev, y_prev, h)
        if method.value == DifferentialEquationSolveMethol.RungeKutt.value:
            return DifferentialEquation.__next_value_runge_kutt(derivative, x_prev, y_prev, h)

    @staticmethod
    def __next_value_euler(derivative: FunctionType, x_prev: float, y_prev: float, h: float) -> float:
        return y_prev + h * derivative(x_prev, y_prev)

    @staticmethod
    def __next_value_modified_euler(derivative: FunctionType, x_prev: float, y_prev: float, h: float) -> float:
        y_ = DifferentialEquation.__next_value_euler(derivative, x_prev, y_prev, h)
        x_ = x_prev + h
        return y_prev + (derivative(x_prev, y_prev) + derivative(x_, y_)) * h / 2

    @staticmethod
    def __next_value_runge_kutt(derivative: FunctionType, x_prev: float, y_prev: float, h: float) -> float:
        k0 = h * derivative(x_prev, y_prev)
        k1 = h * derivative(x_prev + h/2, y_prev + k0/2)
        k2 = h * derivative(x_prev + h/2, y_prev + k1/2)
        k3 = h * derivative(x_prev + h, y_prev + k2)
        return y_prev + (k0 + 2*k1 + 2*k2 + k3)/6

    
