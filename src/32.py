import math

def square_root(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    return math.sqrt(n)

try:
    result = square_root(-1)
except ValueError as e:
    print(e)
