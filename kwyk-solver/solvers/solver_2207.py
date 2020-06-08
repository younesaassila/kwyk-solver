from fractions import Fraction
from functions import int_input


def solve():
    print("Entrez les bornes de l'intervalle [a; b] :")
    a = int_input("a = ")
    b = int_input("b = ")
    x = int_input("Entrez le nombre auquel X est comparé : ")
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
