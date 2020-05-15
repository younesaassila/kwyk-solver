import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    print("Les coordonnées du point A sont :")
    Ax = int_input("Ax = ")
    Ay = int_input("Ay = ")
    Az = int_input("Az = ")
    print("Les coordonnées du vecteur normal n(x; y; z) sont :")
    a = Fraction(int_input("Nx = ")).limit_denominator()
    b = Fraction(int_input("Ny = ")).limit_denominator()
    c = Fraction(int_input("Nz = ")).limit_denominator()
    
    d = Fraction(- (a * Ax) - (b * Ay) - (c * Az)).limit_denominator()
    print(f"Une équation cartésienne de P est {a} x + {b} y + {c} z + {d} = 0")

