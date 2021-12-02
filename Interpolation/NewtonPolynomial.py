from functools import reduce
from types import FunctionType

class NewtonInterpolation:

    @staticmethod
    def make_interpolation(x: list, y: list) -> FunctionType:
        nodes = list(map(lambda i: NewtonInterpolation.__make_Newton_node(x, y, i), range(len(x))))
        return lambda x: NewtonInterpolation.__sum_nodes(x, nodes)
    
    @staticmethod
    def __sum_nodes(x: float, nodes: list):
        return reduce(lambda sum, node: sum + node(x), nodes, 0)
    
    @staticmethod
    def __make_Newton_node(x: list, y: list, node_order: int):
        finite_diff = NewtonInterpolation.__get_finite_diff(x, y, range(node_order + 1))
        x_diffs = NewtonInterpolation.__make_Newton_node_diffs(x, node_order)

        return lambda x: finite_diff * x_diffs(x)
    
    @staticmethod
    def __make_Newton_node_diffs(x: list, max_i: int):
        i = 0
        diffs = []

        while i < max_i:
            diffs.append(NewtonInterpolation.__make_Newton_node_diff(x, i))
            i += 1

        return lambda x: NewtonInterpolation.__prod_diffs(x, diffs)
    
    @staticmethod
    def __get_finite_diff(x: list, y: list, indicies: list):
        order = len(indicies) - 1

        if order == 0:
            return y[indicies[0]]
        elif order > 0:
            left_indicies = indicies[:order]
            right_indicies = indicies[1:]
            return (NewtonInterpolation.__get_finite_diff(x, y, left_indicies) - 
                NewtonInterpolation.__get_finite_diff(x, y, right_indicies)) / (x[indicies[0]] - x[indicies[-1]])
        else:
            return 0
    
    @staticmethod
    def __make_Newton_node_diff(x: list, i: int):
        return lambda x_: x_ - x[i]
    
    @staticmethod
    def __prod_diffs(x: float, diffs: list):
        return reduce(lambda prod, diff: prod * diff(x), diffs, 1)

