import numpy as np
from fractions import Fraction


def solve():
    print("Les coordonnées du point A sont :")
    ax = int(input("Ax = "))
    ay = int(input("Ay = "))
    az = int(input("Az = "))
    print("Les coordonnées du point B sont :")
    bx = int(input("Bx = "))
    by = int(input("By = "))
    bz = int(input("Bz = "))
    print("Les coordonnées du point C sont :")
    cx = int(input("Cx = "))
    cy = int(input("Cy = "))
    cz = int(input("Cz = "))
    print("Les coordonnées du point D sont :")
    dx = int(input("Dx = "))
    dy = int(input("Dy = "))
    dz = int(input("Dz = "))
    # TODO: Simplifier avec numpy
    ABx, ABy, ABz = bx - ax, by - ay, bz - az
    CDx, CDy, CDz = dx - cx, dy - cy, dz - cz
    Dxt, Dyt, Dzt = ABx, ABy, ABz
    Dx, Dy, Dz = ax, ay, az
    D_xt, D_yt, D_zt = CDx, CDy, CDz
    D_x, D_y, D_z = cx, cy, cz
    a = np.array([[Dxt, -D_xt], [Dyt - Dzt, -D_yt - (-D_zt)]])
    b = np.array([(D_x - Dx), ((D_y - Dy) - (D_z - Dz))])
    t1 = np.linalg.solve(a, b)[0]
    x = Fraction(Dxt * t1 + Dx).limit_denominator()
    y = Fraction(Dyt * t1 + Dy).limit_denominator()
    z = Fraction(Dzt * t1 + Dz).limit_denominator()
    print(f"Le point d'intersection des deux droites est M({x}; {y}; {z})")

