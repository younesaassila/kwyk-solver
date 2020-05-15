import numpy as np
from fractions import Fraction


def solve():
    print("Les coordonnées du point A sont :")
    Ax = int(input("Ax = "))
    Ay = int(input("Ay = "))
    Az = int(input("Az = "))
    print("Les coordonnées du point B sont :")
    Bx = int(input("Bx = "))
    By = int(input("By = "))
    Bz = int(input("Bz = "))
    print("Les coordonnées du point C sont :")
    Cx = int(input("Cx = "))
    Cy = int(input("Cy = "))
    Cz = int(input("Cz = "))
    # Calcul des coordonnées du vecteur AB
    ABx = Bx - Ax
    ABy = By - Ay
    ABz = Bz - Az
    # Calcul des coordonnées du vecteur AC
    ACx = Cx - Ax
    ACy = Cy - Ay
    ACz = Cz - Az
    # Produit vectoriel →AB * →AC
    # TODO: Simplifier avec numpy
    a = Fraction((ABy * ACz) - (ACy * ABz)).limit_denominator()
    b = Fraction((ABz * ACx) - (ACz * ABx)).limit_denominator()
    c = Fraction((ABx * ACy) - (ACx * ABy)).limit_denominator()
    d = Fraction(- (a * Ax) - (b * Ay) - (c * Az)).limit_denominator()
    print(f"Une équation cartésienne de P est {a} x + {b} y + {c} z + {d} = 0")

