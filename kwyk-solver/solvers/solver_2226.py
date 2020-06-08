import normale
from functions import float_input

def solve():
    print("X suit la loi normale N(u,o) :")
    u = float_input("u = ")
    o = float_input("o = ")
    norm = normale.normale(u,o)
    print("La question est P(X <= ?)")
    a = float_input("? = ")
    p = round(norm.p_X_inf(a),4)
    print(f"\nP(X <= {a}) = {p}")

