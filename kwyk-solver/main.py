import updater
import os
import re
from functions import int_input, rreplace


version = "1.4"
print("Kwyk Solver")
print(f"Version {version}")

# Vérification de la disponibilité d'une nouvelle version.
# (Cette vérification ne s'effectue que si la version utilisée n'est pas
# une version de développement !)
if not version.endswith("dev"):
    update_info_url = "https://yougi3.github.io/Kwyk-Solver/update_info.json"
    update_info = updater.get_update_info(update_info_url)
    if update_info is not None:
        update_version = update_info["version"]
        if (update_version.strip() != version.strip()):
            print(f"\n/!\\ Une nouvelle mise à jour est disponible (version {update_version}).")
            if input("Souhaitez-vous que le programme se mette à jour ? (o/N) : ").strip().lower() == "o":
                updater.download_and_install(update_info["url"])
            else:
                print("Mise à jour ignorée.")
else:
    print("\n/!\\ Cette version est une version de développement.")
    print("La recherche de mise à jour est ainsi désactivée.")
# Vérifie la présence de fichiers inutilisés de versions antérieures, les
# supprime si possible.
updater.file_cleanup()

if os.path.isdir(f"{os.curdir}/kwyk-solver/solvers/"):
    solvers_directory_path = f"{os.curdir}/kwyk-solver/solvers/"
else:
    # L'utilisateur a lancé le programme en exécutant le fichier main.py.
    # Bien que cela n'est pas recommandé, nous supportons encore pour
    # le moment ce scénario.
    solvers_directory_path = f"{os.curdir}/solvers/"

# Affichage de la liste des exercices supportés en se basant sur les fichiers
# présents dans le dossier 'solvers'.
supported_ex = []
solver_filename_pattern = "solver_([0123456789]+)\.py"
for file in os.listdir(solvers_directory_path):
    solver_filename_match = re.match(solver_filename_pattern, file)
    if solver_filename_match:
        # On récupère le numéro de l'exercice, celui-ci étant inclus dans
        # le nom du fichier.
        supported_ex.append(int(solver_filename_match.group(1)))
# On trie la liste dans l'ordre croissant et on l'affiche à l'utilisateur.
supported_ex.sort()
print(f"\nExercices supportés : {rreplace(str(supported_ex), ',', ' et', 1)[1:-1]}.")

while True:
    prompt = "Entrez le numéro de l'exercice : "
    print(f"\n{'-' * (len(prompt) - 1)}\n")
    ex = int_input(prompt)
    if ex in supported_ex:
        print()
        exec(f"from solvers import solver_{ex}")
        exec(f"solver_{ex}.solve()")
    else:
        print("\n(!) Exercice non supporté par le solveur.")
