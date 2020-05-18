def int_input(prompt = ""):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print(f"Veuillez entrer un nombre entier valide.")


def float_input(prompt = ""):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print(f"Veuillez entrer un nombre décimal valide.")

