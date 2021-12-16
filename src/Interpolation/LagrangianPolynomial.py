from functools import reduce
from types import FunctionType


class LagrangianInterpolation:

    @staticmethod
    def make_interpolation(x: list, y: list) -> FunctionType:
        fundamental_polys = list(map(
            lambda i: LagrangianInterpolation.__make_fundamental_Lagrangian_poly(x, i),
            range(len(y))
        ))

        return lambda x: LagrangianInterpolation.__sum_fundamental_Lagrangian_polys(x, y, fundamental_polys) 

    @staticmethod
    def __sum_fundamental_Lagrangian_polys(x: float, y: list, fundamental_Lagrangian_polys: list):
        return reduce(lambda sum, i: sum + y[i]*fundamental_Lagrangian_polys[i](x), range(len(y)), 0)

    @staticmethod
    def __make_fundamental_Lagrangian_poly(x: list, i):
        elems_to_visit = list(range(len(x)))
        elems_to_visit.pop(i)
    
        nodes = list(map(
            lambda n_elem: LagrangianInterpolation.__make_fundamental_Lagrangian_poly_node(x[i], x[n_elem]),
            elems_to_visit
        ))

        return lambda x: LagrangianInterpolation.__prod_fundamental_Lagrangian_poly_nodes(x, nodes)

    @staticmethod
    def __make_fundamental_Lagrangian_poly_node(current_x: float, other_x: float):
        return lambda x: (x - other_x) / (current_x - other_x)

    @staticmethod
    def __prod_fundamental_Lagrangian_poly_nodes(x: float, nodes: list):
        return reduce(lambda prod, node: prod * node(x), nodes, 1)
