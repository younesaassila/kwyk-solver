from fractions import Fraction
from functions import fraction_input


def solve():
    x = fraction_input("Entrez le nombre auquel X est comparé : ")
    p = fraction_input("Entrez la valeur de la probabilité P : ")
    sign = input(
        "Le signe de la comparaison dans P() est <= ou >= ? ").strip()

    if sign == ">=" or sign == "≥":
        result = f"ln({p})/({- x})"
    elif sign == "<=" or sign == "≤":
        result = f"ln({- p + 1})/({- x})"
    else:
        print("Seuls les symboles <= et >= sont acceptés. Veuillez recommencer.")
        return
    print(f"La paramètre λ est égal à {result}")
