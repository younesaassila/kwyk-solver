from fractions import Fraction
from functions import fraction_input


def solve():
    print("Veuillez entrer la valeur du paramètre p :")
    p = fraction_input("p = ")

    e = Fraction(1 / p).limit_denominator()
    print(f"L'espérance mathématique de p est {e}")

