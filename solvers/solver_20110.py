import numpy as np
from fractions import Fraction


def solve():
    print("Veuillez renseigner les coordonnées du point M :")
    Mx = int(input("Mx = "))
    My = int(input("My = "))
    Mz = int(input("Mz = "))
    print("Veuillez renseigner les coefficients pour chacune des coordonnées de l'équation paramétrique de la droite (d) :")
    Dxt = int(input("x = a + bt, dans ce cas b = "))
    Dyt = int(input("y = a + bt, dans ce cas b = "))
    Dzt = int(input("z = a + bt, dans ce cas b = "))
    location = input("Où se situe l'inconnue ? x, y ou z : ").strip()
    print("Veuillez renseigner les constantes connues pour chacune des coordonnées de l'équation paramétrique de la droite (d) :")
    Dx, Dy, Dz, t = 0, 0, 0, 0
    missing_constant = 0
    if (location == "x"):
        Dy = int(input(f"y = a + {Dyt}t, dans ce cas a = "))
        Dz = int(input(f"z = a + {Dzt}t, dans ce cas a = "))
        t = (My - Dy) / Dyt
        missing_constant = Fraction(-Dxt * t + Mx).limit_denominator()
    elif (location == "y"):
        Dx = int(input(f"x = a + {Dxt}t, dans ce cas a = "))
        Dz = int(input(f"z = a + {Dzt}t, dans ce cas a = "))
        t = (Mz - Dz) / Dzt
        missing_constant = Fraction(-Dyt * t + My).limit_denominator()
    elif (location == "z"):
        Dx = int(input(f"x = a + {Dxt}t, dans ce cas a = "))
        Dy = int(input(f"y = a + {Dyt}t, dans ce cas a = "))
        t = (Mx - Dx) / Dxt
        missing_constant = Fraction(-Dzt * t + Mz).limit_denominator()
    print(f"La constante inconnue en {location} doit être égale à {missing_constant}")

