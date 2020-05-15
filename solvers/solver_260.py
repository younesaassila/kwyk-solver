import numpy as np
from fractions import Fraction


def solve():
    print("première équation du système : ax + by + cz = d")
    a1 = int(input("a = ? "))
    b1 = int(input("b = ? "))
    c1 = int(input("c = ? "))
    d1 = int(input("d = ? "))
    print("deuxième équation du système : ax + by + cz = d")
    a2 = int(input("a = ? "))
    b2 = int(input("b = ? "))
    c2 = int(input("c = ? "))
    d2 = int(input("d = ? "))
    # cas plan
    if (a1/a2 == b1/b2 == c1/c2 == d1/d2):
        print(f"les équations sont équivalentes : le système représente un plan de vecteur normal n({a1};{b1};{c1})")
    # cas doite
    else:
        # la droite a pour vecteur directeur un vecteur prependiculaire au deux vecteurs normaux AKA le produit vectoriel
        print(f"les équations sont différentes : le système représente une droite (ou l'ensemble vide)un vecteur directeur de cette droite est u{np.cross((a1,b1,c1),(a2,b2,c2))}")

