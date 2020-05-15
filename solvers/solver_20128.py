import numpy as np
from fractions import Fraction


def solve():
    print("Les constantes pour chacune des coordonnées de l'équation paramétrique de la droite D sont :")
    Dx = int(input("x = a + bt, dans ce cas a = "))
    Dy = int(input("y = a + bt, dans ce cas a = "))
    Dz = int(input("z = a + bt, dans ce cas a = "))
    print("Les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite D sont :")
    Dxt = int(input(f"x = {Dx} + bt, dans ce cas b = "))
    Dyt = int(input(f"y = {Dy} + bt, dans ce cas b = "))
    Dzt = int(input(f"z = {Dz} + bt, dans ce cas b = "))
    print("Les constantes pour chacune des coordonnées de l'équation paramétrique de la droite D' sont :")
    D_x = int(input("x = a + bt, dans ce cas a = "))
    D_y = int(input("y = a + bt, dans ce cas a = "))
    D_z = int(input("z = a + bt, dans ce cas a = "))
    print("Les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite D' sont :")
    D_xt = int(input(f"x = {D_x} + bt, dans ce cas b = "))
    D_yt = int(input(f"y = {D_y} + bt, dans ce cas b = "))
    D_zt = int(input(f"z = {D_z} + bt, dans ce cas b = "))
    # On résout le système d'équations linéaires.
    a = np.array([[Dxt, -D_xt], [Dyt - Dzt, -D_yt - (-D_zt)]])
    b = np.array([(D_x - Dx), ((D_y - Dy) - (D_z - Dz))])
    t1 = np.linalg.solve(a, b)[0]
    # On calcule les coordonnées du point d'intersection.
    x = Fraction(Dxt * t1 + Dx).limit_denominator()
    y = Fraction(Dyt * t1 + Dy).limit_denominator()
    z = Fraction(Dzt * t1 + Dz).limit_denominator()
    print(f"Le point d'intersection des deux droites est M({x}; {y}; {z})")

