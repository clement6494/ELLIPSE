import requests

# Définir l'URL de l'API et la clé API
url = "https://api.jcdecaux.com/vls/v3/stations"
params = {
    "apiKey": "e0a1bf2c844edb9084efc764c089dd748676cc14",
    "contract": "paris" # Changer ici le nom de la ville souhaitée
}

# Faire la requête à l'API
response = requests.get(url, params=params)
data = response.json()

# Traiter les données
velos_meca = 0
velos_elec = 0
nb_stations = len(data)

for station in data:
    velos_meca += station["mainStands"]["availabilities"]["mechanical"]
    velos_elec += station["mainStands"]["availabilities"]["electrical"]

# Calculer le pourcentage de vélos mécaniques et électriques
pourcentage_meca = round(100 * velos_meca / (velos_meca + velos_elec), 2)
pourcentage_elec = round(100 * velos_elec / (velos_meca + velos_elec), 2)

# Afficher les résultats
print(f"Pourcentage de vélos mécaniques : {pourcentage_meca}%")
print(f"Pourcentage de vélos électriques : {pourcentage_elec}%")
print(f"Nombre de stations : {nb_stations}")