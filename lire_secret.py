import os

token = os.environ.get("SECRET_API_TOKEN")

if not token:
    print("Le secret SECRET_API_TOKEN est absent de l'environnement.")
    raise SystemExit(1)

print("Le secret est bien accessible depuis Python.")
print(f"Longueur du token : {len(token)}")

# Exemple d'utilisation reelle avec un appel API :
# import requests
# headers = {"Authorization": f"Bearer {token}"}
# response = requests.get("https://api.exemple.org/ressource", headers=headers)
