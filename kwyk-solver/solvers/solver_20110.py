import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    print(
        "Les constantes pour chacune des coordonnées de l'équation paramétrique de la droite (d) sont :"
    )
    print("La constante de la coordonnée en x est l'inconnue")
    ya = int_input("y = a + bt, dans ce cas a = ")
    za = int_input("z = a + bt, dans ce cas a = ")
    print(
        "Les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite (d) sont :"
    )
    xb = int_input("x = a + bt, dans ce cas b = ")
    yb = int_input(f"y = {ya} + bt, dans ce cas b = ")
    zb = int_input(f"z = {za} + bt, dans ce cas b = ")
    print("Les coordonnées du point M sont :")
    mx = int_input("Mx = ")
    my = int_input("My = ")
    mz = int_input("Mz = ")

    t = (my - ya) / yb
    xa = Fraction(-xb * t + mx).limit_denominator()
    print(f"La constante inconnue en x doit être égale à {xa}")
