import updater, solvers

version = "1.1"
print(f"\tKwyk Solver version {version}")

# Vérification des mises à jour.
update_info = updater.get_update_info()
if update_info is not None:
  update_version = update_info["version"]
  if (update_version.strip() != version.strip()):
    print(f"\n! Une nouvelle mise à jour est disponible (version {update_version}).")
    if input("Souhaitez-vous la télécharger et l'installer ? (o/N) : ").strip().lower() == "o":
      # Téléchargement de la mise à jour.
      print("Téléchargement de la mise à jour...")
      updater.download_update(update_info["package_url"])

while True:
  print()
  ex = input("Entrez un numéro d'exercice : ")
  if (ex == "20110"):
    solvers.solver_20110()
  elif (ex == "20118"):
    solvers.solver_20118()
  elif (ex == "20119"):
    solvers.solver_20119()
  elif (ex == "20128"):
    solvers.solver_20128()
  elif (ex == "20129"):
    solvers.solver_20129()
  elif (ex == "28036" or ex == "28037"):
    solvers.solver_28036_28037()
  else:
    print("Exercice non supporté par le solveur.")
