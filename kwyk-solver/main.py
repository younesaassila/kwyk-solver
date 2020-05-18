import updater
from functions import int_input


version = "1.3dev"
print("Kwyk Solver".center(80).rstrip())
print(f"Version {version}".center(80).rstrip())

# Vérification de la disponibilité d'une nouvelle version.
# (Cette vérification ne s'effectue que si la version utilisée n'est pas
# une version de développement !)
if not version.endswith("dev"):
    update_info_url = "https://yougi3.github.io/Kwyk-Solver/update_info.json"
    update_info = updater.get_update_info(update_info_url)
    if update_info is not None:
        update_version = update_info["version"]
        if (update_version.strip() != version.strip()):
            print(f"\n\t! Une nouvelle mise à jour est disponible (version {update_version}).")
            if input("Souhaitez-vous la télécharger et l'installer ? (o/N) : ").strip().lower() == "o":
                updater.download_and_install(update_info["url"])
            else:
                print("Mise à jour ignorée.")
else:
    print("\n\t! Avertissement : Cette version est une version de développement.")
    print("La recherche de mise à jour est ainsi désactivée.")

# Vérifie la présence de fichiers inutilisés de versions antérieures, les
# supprime si possible.
updater.file_cleanup()

# Boucle principale du programme : c'est ici que vous pouvez activer le
# support d'un nouvel exercice par le programme.
supported_ex = (260, 20110, 20116, 20118, 20119, 20124, 20128, 20129, 28036, 28037)
print(f"\nExercices supportés : {str(supported_ex)[1:-1]}")

while True:
    print()
    ex = int_input("Entrez le numéro de l'exercice : ")
    if ex in supported_ex:
        print()
        exec(f"from solvers import solver_{ex}")
        exec(f"solver_{ex}.solve()")
    else:
        print("Exercice non supporté par le solveur.")
