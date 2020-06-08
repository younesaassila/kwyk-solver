from fractions import Fraction
from functions import float_input


def solve():
    print("Veuillez entrer la valeur du paramètre p :")
    p = float_input("p = ")

    e = Fraction(1 / p).limit_denominator()
    print(f"L'espérance mathématique de p est {e}")
