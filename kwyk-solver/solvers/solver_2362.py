from fractions import Fraction
from functions import int_input, fraction_input


def solve():
    print("Entrez les valeurs définissant la fonction f(x) = m*x^p :")
    m = fraction_input("m = ")
    p = int_input("p = ")
    print("Entrez les bornes de l'intervalle [a; b] dans lequel se situe X :")
    a = fraction_input("a = ")
    b = fraction_input("b = ")

    def F(x):
        return Fraction((m / (p + 1)) * pow(x, (p + 1))).limit_denominator()
    p_a = F(b) - F(a)
    print(f"La probabilité que X prenne ses valeurs dans [{a}; {b}] est {round(float(p_a), 4)}")

    print(
        f"\nEntrez les bornes de l'intervalle [u; v] dans lequel se situe X sachant qu'il appartient à l'intervalle [{a}; {b}] :")
    u = fraction_input("u = ")
    v = fraction_input("v = ")

    p_b = F(v) - F(u)
    result = p_b / p_a
    print(f"La probabilité P est de {round(float(result), 4)}")
