import numpy as np
from fractions import Fraction


def solve():
    print("Les coefficients de l'équation paramétrique donnée ax + by + cz + d = 0 sont :")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    print("Les coordonnées du point A sont :")
    Ax = int(input("Ax = "))
    Ay = int(input("Ay = "))
    Az = int(input("Az = "))
    print("Les coordonnées du point B sont :")
    Bx = int(input("Bx = "))
    By = int(input("By = "))
    Bz = int(input("Bz = "))
    # Calcul des coordonnées du vecteur AB
    ABx = Bx - Ax
    ABy = By - Ay
    ABz = Bz - Az
    # Vérifions si les points de la droite sont tous les deux inclus dans le plan
    is_a_in_plane = a * Ax + b * Ay + c * Az + d == 0
    is_b_in_plane = a * Bx + b * By + c * Bz + d == 0
    if (is_a_in_plane and is_b_in_plane):
        print("(AB) est incluse dans le plan")
    else:
        # Calcul du produit scalaire entre le vecteur normal au plan et le vecteur AB
        scalar_product = a * ABx + b * ABy + c * ABz
        # Vérification du parallélisme de (AB) au plan
        if (scalar_product == 0):
            print("(AB) est parallèle au plan")
        else:
            # La droite (AB) est sécante au plan
            print("(AB) est sécante au plan")
            # Calculons le point d'intersection
            t = ((-a * Ax) + (-b * Ay) + (-c * Az) + (-d)) / ((a * ABx) + (b * ABy) + (c * ABz))
            Mx = Fraction(ABx * t + Ax).limit_denominator()
            My = Fraction(ABy * t + Ay).limit_denominator()
            Mz = Fraction(ABz * t + Az).limit_denominator()
            print(f"Le point d'intersection du plan et de la droite (AB) est M({Mx}; {My}; {Mz})")
            # Vérifions si (AB) et le plan sont orthogonaux
            if (ABx == 0 or ABy == 0 or ABz == 0):
                print("(AB) et le plan NE sont PAS orthogonaux")
            else:
                if ((a / ABx) == (b / ABy) == (c / ABz)):
                    print("(AB) et le plan sont orthogonaux")
                else:
                    print("(AB) et le plan NE sont PAS orthogonaux")

