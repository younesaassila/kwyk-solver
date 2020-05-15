import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    print("Les coordonnées du point A sont :")
    Ax = int_input("Ax = ")
    Ay = int_input("Ay = ")
    Az = int_input("Az = ")
    print("Les coordonnées du point B sont :")
    Bx = int_input("Bx = ")
    By = int_input("By = ")
    Bz = int_input("Bz = ")
    print("Les coordonnées du point C sont :")
    Cx = int_input("Cx = ")
    Cy = int_input("Cy = ")
    Cz = int_input("Cz = ")

    AB = np.array([Bx - Ax, By - Ay, Bz - Az])
    AC = np.array([Cx - Ax, Cy - Ay, Cz - Az])
    vector_product = np.cross(AB, AC)

    a = Fraction(vector_product[0]).limit_denominator()
    b = Fraction(vector_product[1]).limit_denominator()
    c = Fraction(vector_product[2]).limit_denominator()
    d = Fraction(- (a * Ax) - (b * Ay) - (c * Az)).limit_denominator()
    
    print(f"Une équation cartésienne de P est {a} x + {b} y + {c} z + {d} = 0")

