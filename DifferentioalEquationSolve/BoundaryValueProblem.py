from types import FunctionType
from DifferrentialEquation import DifferentialEquation, DifferentialEquationSolveMethol


class BoundaryValueProblem:

    @staticmethod
    def solve(
        dy_dx: FunctionType,
        p: FunctionType,
        q: FunctionType,
        f: FunctionType,
        alphas: list,
        betas: list,
        a: float,
        b: float,
        h: float) -> list:
        
        y_list, x_list = DifferentialEquation.solve(dy_dx, a, b, )
