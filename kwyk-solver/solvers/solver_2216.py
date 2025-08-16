from fractions import Fraction
from functions import int_input, float_input


def solve():
    print("La question est p(x ≤ t)")
    t = int_input("t = ")

    print(f"La probabilité p(x ≤ {t}) est égale à 1-e^(-{t}a)")

    print(
        "\nEntrez la valeur maximale que peut prendre la probabilité p, dans le dernier paragraphe (c'est un nombre décimal)"
    )
    m = float_input("m = ")

    print(f"L'intervalle est ]0; ln({Fraction(- m + 1).limit_denominator()})/(-{t})]")
