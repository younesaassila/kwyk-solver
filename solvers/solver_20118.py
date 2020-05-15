import numpy as np
from fractions import Fraction


def solve():
    print("Les coordonnées du point A sont :")
    Ax = int(input("Ax = "))
    Ay = int(input("Ay = "))
    Az = int(input("Az = "))
    print("Les coordonnées du vecteur normal n sont :")
    a = Fraction(int(input("Nx = "))).limit_denominator()
    b = Fraction(int(input("Ny = "))).limit_denominator()
    c = Fraction(int(input("Nz = "))).limit_denominator()
    d = Fraction(- (a * Ax) - (b * Ay) - (c * Az)).limit_denominator()
    print(f"Une équation cartésienne de P est {a} x + {b} y + {c} z + {d} = 0")

