import urllib.request, json, requests, zipfile, io, sys
from urllib.error import HTTPError, URLError

# Retourne les données de la dernière mise à jour disponible.
def get_update_info():
  update_info_url = "https://yougi3.github.io/Kwyk-Solver/update_info.json"
  update_info = None
  try:
    with urllib.request.urlopen(update_info_url) as url:
      update_info = json.loads(url.read().decode())
  except HTTPError as e:
    print(f"Erreur : Le serveur n'a pas pu répondre à la requête lors de la vérification des mises à jour disponibles.")
    print(f"Code d'erreur : {e.code}")
  except URLError as e:
    print(f"Erreur : Impossible de joindre le serveur afin de vérifier les mises à jour disponibles.")
    print(f"Raison : {e.reason}")
  return update_info

# Télécharge et décompresse le dossier ZIP contenant la dernière version.
def update(url):
  print("Téléchargement de la mise à jour...")
  package = requests.get(url)
  print("Téléchargement terminé.")
  print("Installation de la mise à jour...")
  zipfile.ZipFile(io.BytesIO(package.content)).extractall()
  print("Installation terminé.")
  print("La mise à jour est terminée ! Le programme doit redémarrer.")
  input("Appuyez sur une touche pour le fermer puis réouvrez-le manuellement.")
  sys.exit("Le programme s'arrête...")
