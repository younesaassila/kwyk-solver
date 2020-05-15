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
    print("Les coordonnées du point D sont :")
    Dx = int_input("Dx = ")
    Dy = int_input("Dy = ")
    Dz = int_input("Dz = ")
    
    AB = np.array([Bx - Ax, By - Ay, Bz - Az])
    CD = np.array([Dx - Cx, Dy - Cy, Dz - Cz])
    m1 = np.array([[AB[0], -CD[0]], [AB[1] - AB[2], -CD[1] - (-CD[2])]])
    m2 = np.array([(Cx - Ax), ((Cy - Ay) - (Cz - Az))])
    t1 = np.linalg.solve(m1, m2)[0]
    x = Fraction(AB[0] * t1 + Ax).limit_denominator()
    y = Fraction(AB[1] * t1 + Ay).limit_denominator()
    z = Fraction(AB[2] * t1 + Az).limit_denominator()
    print(f"Le point d'intersection des deux droites est M({x}; {y}; {z})")

