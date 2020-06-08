import normale
from functions import float_input

def solve():
    print("X suit la loi normale N(u, o) :")
    u = float_input("u = ")
    o = float_input("o = ")
    norm = normale.normale(u, o)
    print("La question est P(a ≤ X ≤ b)")
    a = float_input("a = ")
    b = float_input("b = ")
    p = round(norm.p_X_btw(a, b), 4)
    print(f"\nP({a} <= X <= {b}) = {p}")

