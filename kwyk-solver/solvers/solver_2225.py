from fractions import Fraction
from functions import float_input, fraction_input


def solve():
    p = fraction_input("Entrez le paramètre de la loi exponentielle : ")
    print("Entrez les bornes de l'intervalle P(u ≤ X ≤ v) :")
    u = float_input("u = ")
    v = float_input("v = ")

    exponent_u = Fraction(- p * u).limit_denominator()
    exponent_v = Fraction(- p * v).limit_denominator()
    result = f"e^({exponent_u}) - e^({exponent_v})"
    print(f"\nLa probabilité P est de {result}")

