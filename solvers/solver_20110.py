import numpy as np
from fractions import Fraction
from functions import int_input


def solve():
    print("Les coordonnées du point M sont :")
    Mx = int_input("Mx = ")
    My = int_input("My = ")
    Mz = int_input("Mz = ")
    print("Les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite (d) sont :")
    Xb = int_input("x = a + bt, dans ce cas b = ")
    Yb = int_input("y = a + bt, dans ce cas b = ")
    Zb = int_input("z = a + bt, dans ce cas b = ")
    print("Les constantes pour chacune des coordonnées de l'équation paramétrique de la droite (d) sont :")
    print("La constante de la coordonnée en x est l'inconnue")
    Ya = int_input(f"y = a + {Yb}t, dans ce cas a = ")
    Za = int_input(f"z = a + {Zb}t, dans ce cas a = ")
    
    t = (My - Ya) / Yb
    Xa = Fraction(-Xb * t + Mx).limit_denominator()
    print(f"La constante inconnue en x doit être égale à {Xa}")

