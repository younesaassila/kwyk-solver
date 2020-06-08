import math
from fractions import Fraction
from functions import int_input


def get_exponential_distribution_parameter():
    while True:
        try:
            return Fraction(input("Entrez le paramètre de la loi exponentielle : "))
        except ValueError:
            print("Veuillez entrer un nombre valide (celui-ci peut être sous forme de fraction).")
            continue


def solve():
    p = get_exponential_distribution_parameter()
    x = int_input("Entrez le nombre auquel X est comparé : ")
    sign = input(
        "Le signe de la comparaison dans P() est <= ou >= ? ").strip()

    exponent = Fraction(- p * x).limit_denominator()
    if sign == ">=" or sign == "≥":
        result = f"e^({exponent})"
    elif sign == "<=" or sign == "≤":
        result = f"1 - e^({exponent})"
    else:
        print("Seuls les symboles <= et >= sont acceptés. Veuillez recommencez.")
        return
    print(f"La probabilité P est de {result}")
