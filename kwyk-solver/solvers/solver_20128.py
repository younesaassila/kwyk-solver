import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    print("Les constantes pour chacune des coordonnées de l'équation paramétrique de la droite D sont :")
    x1a = int_input("x = a + bt, dans ce cas a = ")
    y1a = int_input("y = a + bt, dans ce cas a = ")
    z1a = int_input("z = a + bt, dans ce cas a = ")
    print("Les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite D sont :")
    x1b = int_input(f"x = {x1a} + bt, dans ce cas b = ")
    y1b = int_input(f"y = {y1a} + bt, dans ce cas b = ")
    z1b = int_input(f"z = {z1a} + bt, dans ce cas b = ")
    print("Les constantes pour chacune des coordonnées de l'équation paramétrique de la droite D' sont :")
    x2a = int_input("x = a + bt, dans ce cas a = ")
    y2a = int_input("y = a + bt, dans ce cas a = ")
    z2a = int_input("z = a + bt, dans ce cas a = ")
    print("Les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite D' sont :")
    x2b = int_input(f"x = {x2a} + bt, dans ce cas b = ")
    y2b = int_input(f"y = {y2a} + bt, dans ce cas b = ")
    z2b = int_input(f"z = {z2a} + bt, dans ce cas b = ")
    
    # On résout le système d'équations linéaires.
    m1 = np.array([[x1b, - x2b], [y1b - z1b, - y2b + z2b]])
    m2 = np.array([(x2a - x1a), (y2a - y1a - z2a + z1a)])
    t1 = np.linalg.solve(m1, m2)[0]
    # On calcule les coordonnées du point d'intersection.
    x = Fraction(x1b * t1 + x1a).limit_denominator()
    y = Fraction(y1b * t1 + y1a).limit_denominator()
    z = Fraction(z1b * t1 + z1a).limit_denominator()
    print(f"Le point d'intersection des deux droites est M({x}; {y}; {z})")

