import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    print("Les coordonnées du point A sont :")
    ax = int_input("Ax = ")
    ay = int_input("Ay = ")
    az = int_input("Az = ")
    print("Les coordonnées du point B sont :")
    bx = int_input("Bx = ")
    by = int_input("By = ")
    bz = int_input("Bz = ")
    print("Les coordonnées du point C sont :")
    cx = int_input("Cx = ")
    cy = int_input("Cy = ")
    cz = int_input("Cz = ")

    AB = np.array([bx - ax, by - ay, bz - az])
    AC = np.array([cx - ax, cy - ay, cz - az])
    vector_product = np.cross(AB, AC)

    a = Fraction(vector_product[0]).limit_denominator()
    b = Fraction(vector_product[1]).limit_denominator()
    c = Fraction(vector_product[2]).limit_denominator()
    d = Fraction(- (a * ax) - (b * ay) - (c * az)).limit_denominator()
    
    print(f"Une équation cartésienne de P est {a} x + {b} y + {c} z + {d} = 0")

