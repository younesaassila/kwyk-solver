import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    print("Les coefficients de la première équation ax + by + cz = d du système sont :")
    a1 = int_input("a = ")
    b1 = int_input("b = ")
    c1 = int_input("c = ")
    d1 = int_input("d = ")
    print("Les coefficients de la deuxième équation ax + by + cz = d du système sont :")
    a2 = int_input("a = ")
    b2 = int_input("b = ")
    c2 = int_input("c = ")
    d2 = int_input("d = ")

    # Cas du plan :
    if (a1 / a2) == (b1 / b2) == (c1 / c2) == (d1 / d2):
        print(
            f"Les équations sont équivalentes, le système représente donc un plan de vecteur normal n({a1}; {b1}; {c1})"
        )
    # Cas de la droite :
    else:
        # La droite a pour vecteur directeur un vecteur perpendiculaire au deux vecteurs normaux (produit vectoriel)
        vector_product = np.cross((a1, b1, c1), (a2, b2, c2))
        print(
            f"Les équations sont différentes, le système représente donc une droite (ou l'ensemble vide)"
        )
        print(
            f"Un vecteur directeur de cette droite est u({vector_product[0]}; {vector_product[1]}; {vector_product[2]})"
        )
