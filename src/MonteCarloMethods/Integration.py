from types import FunctionType
import numpy as np
from functools import reduce

class Integration:

    @staticmethod
    def calculate(bounds: list, function: FunctionType, n: int) -> float:
        bottom_bounds = list(map(lambda bound: bound[0], bounds))
        top_bounds = list(map(lambda bound: bound[1], bounds))
        n_args = len(bounds)
        args = np.transpose([ np.random.uniform(bottom_bounds[i], top_bounds[i], n) for i in range(n_args) ])
        function_mean = reduce(lambda f_sum, args: f_sum + function(args), args, 0) / n
        bound_factor = reduce(lambda factor_prod, i: factor_prod * (top_bounds[i] - bottom_bounds[i]), list(range(n_args)), 1)
        return bound_factor * function_mean

