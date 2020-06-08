from fractions import Fraction
from functions import int_input, float_input


def solve():
    t = int_input("Entrez le nombre d'années de la mission : ")

    print(f"La probabilité p(x ≤ {t}) est égale à 1-e^(-{t}a)")

    l = float_input("\nEntrez la valeur maximale de la probabilité de p : ")

    print(f"L'intervalle est ]0; ln({Fraction(- l + 1).limit_denominator()})/(-{t})]")

