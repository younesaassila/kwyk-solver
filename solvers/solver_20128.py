import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    print("Les constantes pour chacune des coordonnées de l'équation paramétrique de la droite D sont :")
    Xa1 = int_input("x = a + bt, dans ce cas a = ")
    Ya1 = int_input("y = a + bt, dans ce cas a = ")
    Za1 = int_input("z = a + bt, dans ce cas a = ")
    print("Les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite D sont :")
    Xb1 = int_input(f"x = {Xa1} + bt, dans ce cas b = ")
    Yb1 = int_input(f"y = {Ya1} + bt, dans ce cas b = ")
    Zb1 = int_input(f"z = {Za1} + bt, dans ce cas b = ")
    print("Les constantes pour chacune des coordonnées de l'équation paramétrique de la droite D' sont :")
    Xa2 = int_input("x = a + bt, dans ce cas a = ")
    Ya2 = int_input("y = a + bt, dans ce cas a = ")
    Za2 = int_input("z = a + bt, dans ce cas a = ")
    print("Les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite D' sont :")
    Xb2 = int_input(f"x = {Xa2} + bt, dans ce cas b = ")
    Yb2 = int_input(f"y = {Ya2} + bt, dans ce cas b = ")
    Zb2 = int_input(f"z = {Za2} + bt, dans ce cas b = ")
    # On résout le système d'équations linéaires.
    m1 = np.array([[Xb1, - Xb2], [Yb1 - Zb1, - Yb2 + Zb2]])
    m2 = np.array([(Xa2 - Xa1), (Ya2 - Ya1 - Za2 + Za1)])
    t1 = np.linalg.solve(m1, m2)[0]
    # On calcule les coordonnées du point d'intersection.
    x = Fraction(Xb1 * t1 + Xa1).limit_denominator()
    y = Fraction(Yb1 * t1 + Ya1).limit_denominator()
    z = Fraction(Zb1 * t1 + Za1).limit_denominator()
    print(f"Le point d'intersection des deux droites est M({x}; {y}; {z})")

