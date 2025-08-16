from fractions import Fraction
from functions import int_input, fraction_input


def solve():
    print("La question est :")
    print("\t1. P(X ≤ a)")
    print("\t2. P(X ≥ a)")
    choix = 0
    while not choix in [1, 2]:
        choix = int_input("1 ou 2 ? ")
    a = fraction_input("a = ")
    p = fraction_input("Entrez la valeur de la probabilité P : ")

    if choix == 1:
        result = f"ln({- p + 1})/({- a})"
    else:
        result = f"ln({p})/({- a})"
    print(f"\nLa paramètre λ est égal à {result}")
