import normale
from functions import float_input, int_input

def solve():
    print("X suit la loi normale N(u,o) :")
    u = float_input("u = ")
    o = float_input("o = ")
    norm = normale.normale(u,o)
    print("La question est :")
    print("1. P(X <= a)")
    print("2. P(X >= a)")

    choix=0
    while not choix in [1,2] : choix = int_input("1/2 :")
    a = float_input("a = ")
    
    if choix == 1 : p = round(norm.p_X_inf(a),4)
    if choix == 2 : p = round(norm.p_X_sup(a),4)

    print(f"\nP(X <= {a}) = {p}")

