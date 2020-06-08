from fractions import Fraction


# Demande à l'utilisateur l'entrée d'un nombre entier tant que celui-ci n'entre
# pas un nombre entier valide.
def int_input(prompt = ""):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"Veuillez entrer un nombre entier valide.")


# Demande à l'utilisateur l'entrée d'un nombre décimal tant que celui-ci
# n'entre pas un nombre décimal valide.
def float_input(prompt = ""):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"Veuillez entrer un nombre décimal valide.")


# Remplace les dernières occurrences d'un caractère dans la chaîne donnée.
def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


# Demande à l'utilisateur l'entrée d'un nombre (entier, décimal, fraction)
# tant que celui-ci n'est pas valide. Retourne un object Fraction.
def get_exponential_distribution_parameter():
    while True:
        try:
            return Fraction(input("Entrez le paramètre de la loi exponentielle : "))
        except ValueError:
            print(
                "Veuillez entrer un nombre valide (celui-ci peut être sous forme de fraction).")
            continue
