import requests
import zipfile
import io
import sys


# Retourne les données concernant la dernière mise à jour disponible.
def get_update_info(url):
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        print("\n! La recherche de mise à jour a échoué.")
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

