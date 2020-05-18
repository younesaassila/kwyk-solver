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

