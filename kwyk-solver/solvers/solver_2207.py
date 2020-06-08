from fractions import Fraction
from functions import float_input


def solve():
    print("Entrez les bornes de l'intervalle [a; b] :")
    a = float_input("a = ")
    b = float_input("b = ")
    x = float_input("Entrez le nombre auquel X est comparé : ")
    sign = input(
        "Le signe de la comparaison dans P() est <= ou >= ? ").strip()
    
    if sign == ">=" or sign == "≥":
        result = Fraction(abs(b - x) * (1 / (b - a))).limit_denominator()
    elif sign == "<=" or sign == "≤":
        result = Fraction(abs(x - a) * (1 / (b - a))).limit_denominator()
    else:
        print("Seuls les symboles <= et >= sont acceptés. Veuillez recommencez.")
        return
    print(f"La probabilité P est de {result}")
