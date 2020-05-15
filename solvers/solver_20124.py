import numpy as np
from fractions import Fraction


def solve():
    for i in range(4):
        print("u(x,y,z)")
        x1 = int(input("x = ? "))
        y1 = int(input("y = ? "))
        z1 = int(input("z = ? "))
        print("v(x,y,z)")
        x2 = int(input("x = ? "))
        y2 = int(input("y = ? "))
        z2 = int(input("z = ? "))
        if np.dot((x1, y1, z1), (x2, y2, z2)) == 0:
            print("Orthogonaux")
        else:
            print("Non orthogonaux")

