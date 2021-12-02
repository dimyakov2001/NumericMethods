from types import FunctionType

def choose_start_point(f: FunctionType, d2f_dx2: FunctionType, a: float, b: float) -> float:
    a_value = f(a) * d2f_dx2(a)
    if a_value > 0:
        return a
    return b

def length(a: float, b: float) -> float:
    return abs(a - b)

def solve(f: FunctionType, df_dx: FunctionType, d2f_dx2: FunctionType, a: float, b: float, e: float) -> float:
    x_k = choose_start_point(f, d2f_dx2, a, b)
    stop_condition = False

    while not stop_condition:
        x_k_plus = x_k - f(x_k) / df_dx(x_k)

        if length(x_k, x_k_plus) < e:
            stop_condition = True
        x_k = x_k_plus

    return x_k
