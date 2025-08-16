from fractions import Fraction
from functions import int_input, float_input


def solve():
    print("Entrez les bornes de l'intervalle [a; b] :")
    a = float_input("a = ")
    b = float_input("b = ")
    print("La question est :")
    print("\t1. P(X ≤ y)")
    print("\t2. P(X ≥ y)")
    choix = 0
    while not choix in [1, 2]:
        choix = int_input("1 ou 2 ? ")
    y = float_input("y = ")

    if choix == 1:
        result = Fraction(abs(y - a) * (1 / (b - a))).limit_denominator()
    else:
        result = Fraction(abs(b - y) * (1 / (b - a))).limit_denominator()
    print(f"\nLa probabilité P est de {result}")
