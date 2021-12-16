from types import FunctionType

def phi(f: FunctionType, x: float, m: float) -> float:
    return x - f(x) / m

def calculate_M(df_dx: FunctionType, x: float) -> float:
    return 1.01 * df_dx(x)

def length(a: float, b: float) -> float:
    return abs(a - b)

def solve(f: FunctionType, df_dx: FunctionType, x0: float, e: float):
    x_k = x0
    M = calculate_M(df_dx, x_k)
    stop_condition = False

    while not stop_condition:
        x_k_plus = phi(f, x_k, M)
        if length(x_k, x_k_plus) < e:
            stop_condition = True
        x_k = x_k_plus
    return x_k
