from fractions import Fraction
from functions import float_input


def solve():
    print("Entrez les bornes de l'intervalle [a; b] :")
    a = float_input("a = ")
    b = float_input("b = ")
    print("Entrez les bornes de l'intervalle u ≤ X ≤ v :")
    u = float_input("u = ")
    v = float_input("v = ")
    
    result = Fraction(abs(v - u) * (1 / (b - a))).limit_denominator()
    print(f"La probabilité P est de {result}")

