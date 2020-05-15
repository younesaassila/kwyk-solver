import urllib.request, json, requests, zipfile, io
from urllib.error import HTTPError, URLError

# Retourne les données de la dernière mise à jour disponible.
def get_update_info():
  update_url = "https://yougi3.github.io/Kwyk-Solver/update.json"
  update_info = None
  try:
    with urllib.request.urlopen(update_url) as url:
      update_info = json.loads(url.read().decode())
  except HTTPError as e:
    print(f"Erreur : Le serveur n'a pas pu répondre à la requête lors de la vérification des mises à jour disponibles.")
    print(f"Code d'erreur : {e.code}")
  except URLError as e:
    print(f"Erreur : Impossible de joindre le serveur afin de vérifier les mises à jour disponibles.")
    print(f"Raison : {e.reason}")
  return update_info

# Télécharge le dossier compressé contenant la dernière version.
def download_update(url):
  r = requests.get(url)
  z = zipfile.ZipFile(io.BytesIO(r.content))
  z.extractall()
