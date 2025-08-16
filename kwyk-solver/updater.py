import requests
import zipfile
import io
import sys
import os
import shutil


# Retourne les données concernant la dernière mise à jour disponible.
def get_update_info(url):
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        print("\n(!) La recherche de mise à jour a échoué.")
        return None


# Télécharge et décompresse le dossier ZIP contenant la dernière version.
def download_and_install(download_url):
    print("Téléchargement de la mise à jour...")
    package = requests.get(download_url)
    print("Téléchargement terminé.")
    print("Installation de la mise à jour...")
    zipfile.ZipFile(io.BytesIO(package.content)).extractall()
    print("Installation terminé.")
    print("La mise à jour est terminée ! Le programme doit redémarrer.")
    input("Appuyez sur une touche pour le fermer puis réouvrez-le manuellement.")
    sys.exit("Le programme s'arrête...")


# Supprime les fichiers inutilisés de versions antérieures.
def file_cleanup():
    # Versions 1.2 et antérieures.
    if os.path.exists("Kwyk_Solver_Windows.cmd"):
        # Supprime les fichiers functions.py, main.py et updater.py.
        functionsPythonFile = "functions.py"
        mainPythonFile = "main.py"
        updaterPythonFile = "updater.py"
        if os.path.exists(functionsPythonFile):
            os.remove(functionsPythonFile)
        if os.path.exists(mainPythonFile):
            os.remove(mainPythonFile)
        if os.path.exists(updaterPythonFile):
            os.remove(updaterPythonFile)
        # Supprime le répertoire 'solvers'.
        shutil.rmtree("solvers")
        # Supprime les fichiers Kwyk_Solver_Windows.cmd et Installation_Windows.cmd.
        startBatchFile = "Kwyk_Solver_Windows.cmd"
        installBatchFile = "Installation_Windows.cmd"
        if os.path.exists(startBatchFile):
            os.remove(startBatchFile)
        if os.path.exists(installBatchFile):
            os.remove(installBatchFile)
        print(
            "\n(i) Des fichiers inutilisés appartenants à des versions antérieures ont été automatiquement supprimés."
        )
