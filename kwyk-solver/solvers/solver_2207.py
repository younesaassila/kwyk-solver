from fractions import Fraction
from functions import int_input, float_input


def solve():
    print("Entrez les bornes de l'intervalle [a; b] :")
    a = float_input("a = ")
    b = float_input("b = ")
    x = float_input("Entrez le nombre auquel X est comparé : ")
    print("La question est :")
    print("\t1. P(X <= a)")
    print("\t2. P(X >= a)")
    choix = 0
    while not choix in [1, 2]:
        choix = int_input("1 ou 2 ? ")
    
    if choix == 1:
        result = Fraction(abs(x - a) * (1 / (b - a))).limit_denominator()  
    else:
        result = Fraction(abs(b - x) * (1 / (b - a))).limit_denominator()
    print(f"La probabilité P est de {result}")

