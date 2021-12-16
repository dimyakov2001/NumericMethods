from types import FunctionType

def length(a: float, b: float) -> float:
    return abs(a - b)

def have_different_signs(a: float, b: float) -> bool:
    return a * b < 0

def middle(a: float, b: float) -> float:
    return (a + b) / 2

def solve(f: FunctionType, a: float, b: float, e: float) -> float:
    x0 = middle(a, b)
    while length(a, b) >= e:
        if have_different_signs(f(a), f(x0)):
            b = x0
        elif have_different_signs(f(b), f(x0)):
            a = x0
        x0 = middle(a, b)
    return x0
