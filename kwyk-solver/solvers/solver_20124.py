import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    for i in range(4):
        print(f"\tCouple n°{i + 1}")
        print("Les coordonnées du vecteur normal u(x; y; z) sont :")
        x1 = int_input("x = ")
        y1 = int_input("y = ")
        z1 = int_input("z = ")
        print("Les coordonnées du vecteur normal v(x; y; z) sont :")
        x2 = int_input("x = ")
        y2 = int_input("y = ")
        z2 = int_input("z = ")

        scalar_product = np.dot((x1, y1, z1), (x2, y2, z2))
        if scalar_product == 0:
            print("Les deux plans sont orthogonaux")
        else:
            print("Les deux plans NE sont PAS orthogonaux")

