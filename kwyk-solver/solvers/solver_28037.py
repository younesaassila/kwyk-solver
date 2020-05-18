import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    print("Les coefficients de l'équation paramétrique donnée ax + by + cz + d = 0 sont :")
    a = int_input("a = ")
    b = int_input("b = ")
    c = int_input("c = ")
    d = int_input("d = ")
    print("Les coordonnées du point A sont :")
    ax = int_input("Ax = ")
    ay = int_input("Ay = ")
    az = int_input("Az = ")
    print("Les coordonnées du point B sont :")
    bx = int_input("Bx = ")
    by = int_input("By = ")
    bz = int_input("Bz = ")

    AB = np.array([bx - ax, by - ay, bz - az])
    # Vérifions si les points de la droite sont tous les deux inclus dans le plan
    a_in_plane = a * ax + b * ay + c * az + d == 0
    b_in_plane = a * bx + b * by + c * bz + d == 0
    if (a_in_plane and b_in_plane):
        print("(AB) est incluse dans le plan")
    else:
        # Calcul du produit scalaire entre le vecteur normal au plan et le vecteur AB
        scalar_product = a * AB[0] + b * AB[1] + c * AB[2]
        # Vérification du parallélisme de (AB) au plan
        if (scalar_product == 0):
            print("(AB) est parallèle au plan")
        else:
            # La droite (AB) est sécante au plan
            print("(AB) est sécante au plan")
            # Calculons le point d'intersection
            t = ((-a * ax) + (-b * ay) + (-c * az) + (-d)) / ((a * AB[0]) + (b * AB[1]) + (c * AB[2]))
            Mx = Fraction(AB[0] * t + ax).limit_denominator()
            My = Fraction(AB[1] * t + ay).limit_denominator()
            Mz = Fraction(AB[2] * t + az).limit_denominator()
            print(f"Le point d'intersection du plan et de la droite (AB) est M({Mx}; {My}; {Mz})")
            # Vérifions si (AB) et le plan sont orthogonaux
            if (AB[0] == 0 or AB[1] == 0 or AB[2] == 0):
                print("(AB) et le plan NE sont PAS orthogonaux")
            else:
                if ((a / AB[0]) == (b / AB[1]) == (c / AB[2])):
                    print("(AB) et le plan sont orthogonaux")
                else:
                    print("(AB) et le plan NE sont PAS orthogonaux")

