import numpy as np
from fractions import Fraction


def solve():
    # solveur de AX = B
    #a = np.array([[3,1], [1,2]])
    #b = np.array([9,8])
    #x = np.linalg.solve(a, b)
    print("u(x,y,z)")
    x1 = int(input("x = ? "))
    print("Uy est l'inconnue")
    z1 = int(input("z = ? "))
    print("v(x,y,z)")
    x2 = int(input("x = ? "))
    y2 = int(input("y = ? "))
    z2 = int(input("z = ? "))
    print(f"Uy = {Fraction(float(-x1*x2-z1*z2)/float(y2)).limit_denominator()}")

