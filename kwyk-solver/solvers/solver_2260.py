import normale
from functions import float_input


def solve():
    print("X suit la loi normale N(u, o) :")
    v = float_input("u = ")
    o = float_input("o = ")
    norm = normale.Normale(v, o)
    print(f"La question est P({v}-u < X < {v}+u) = a")
    a = float_input("a = ")

    u = 0.5005
    # recherche bourrin à 10^-3 pres, la dichotomie c'est nul anyway
    while norm.p_X_btw(v - u, v + u) < a:
        u += 0.001  # pousser la limite quand la proba est trop petite
    while norm.p_X_btw(v - u, v + u) > a:
        u -= 0.001  # idem quand trop grande

    u = round(u, 2)
    print(f"\nLa valeur de u est {u}")
