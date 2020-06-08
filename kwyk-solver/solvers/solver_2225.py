from fractions import Fraction
from functions import float_input, get_exponential_distribution_parameter


def solve():
    p = get_exponential_distribution_parameter()
    print("Entrez les bornes de l'intervalle P(u ≤ X ≤ v) :")
    u = float_input("u = ")
    v = float_input("v = ")

    exponent_u = Fraction(- p * u).limit_denominator()
    exponent_v = Fraction(- p * v).limit_denominator()
    result = f"e^({exponent_u}) - e^({exponent_v})"
    print(f"La probabilité P est de {result}")
