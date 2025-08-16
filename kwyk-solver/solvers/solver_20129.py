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
    print("Les coordonnées du point D sont :")
    dx = int_input("Dx = ")
    dy = int_input("Dy = ")
    dz = int_input("Dz = ")

    AB = np.array([bx - ax, by - ay, bz - az])
    CD = np.array([dx - cx, dy - cy, dz - cz])
    m1 = np.array([[AB[0], -CD[0]], [AB[1] - AB[2], -CD[1] - (-CD[2])]])
    m2 = np.array([(cx - ax), ((cy - ay) - (cz - az))])
    t1 = np.linalg.solve(m1, m2)[0]
    x = Fraction(AB[0] * t1 + ax).limit_denominator()
    y = Fraction(AB[1] * t1 + ay).limit_denominator()
    z = Fraction(AB[2] * t1 + az).limit_denominator()
    print(f"Le point d'intersection des deux droites est M({x}; {y}; {z})")
