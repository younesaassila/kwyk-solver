import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    print("Les coordonnées du vecteur u(x; y; z) sont :")
    x1 = int_input("x = ")
    print("La coordonnée en y est l'inconnue")
    z1 = int_input("z = ")
    print("Les coordonnées du vecteur v(x; y; z) sont :")
    x2 = int_input("x = ")
    y2 = int_input("y = ")
    z2 = int_input("z = ")
    
    y1 = Fraction(float(- (x1 * x2) - (z1 * z2)) / float(y2)).limit_denominator()
    print(f"La coordonnée en y doit être égale à {y1}")

