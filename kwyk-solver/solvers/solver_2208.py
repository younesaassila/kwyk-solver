from fractions import Fraction
from functions import int_input


def solve():
    print("Entrez les bornes de l'intervalle [a; b] :")
    a = int_input("a = ")
    b = int_input("b = ")
    print("Entrez les bornes de l'intervalle u ≤ X ≤ v :")
    u = int_input("u = ")
    v = int_input("v = ")
    
    result = Fraction(abs(v - u) * (1 / (b - a))).limit_denominator()
    print(f"La probabilité P est de {result}")
