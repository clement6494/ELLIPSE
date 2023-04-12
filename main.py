import urllib.request
import json


# Define the URL for the JCDecaux API and the parameters

api_key = "e0a1bf2c844edb9084efc764c089dd748676cc14"
contract = "lyon"



def cities():
    """recupère et créer un tableau avec touts les villes équipés du système de traquage JCDécaux"""
    #url requete
    url = f"https://api.jcdecaux.com/vls/v3/contracts?apiKey={api_key}"

    #lecture de la reponse de l'API
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())

    #creation du tableau
    villes = {}
    for ville in data:
        villes[ville["name"]] = ville["name"]

    return villes



def veloCount(ville):
    """recupère le nombre de vélos dans une ville"""

    #url requete
    url = f"https://api.jcdecaux.com/vls/v3/stations?contract={ville}&apiKey={api_key}"

    #lecture de la reponse de l'API
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())

    #comptage des velos
    velos=0
    for station in data:
        try:
            velos+= station["totalStands"]["availabilities"]["bikes"]
        except KeyError:
            pass

        

    return velos



def percentage(contract):
    """calcule des données simples sur une ville comme le nombre de velos et la part de mécaniques et electriques"""

    #url requete
    url = f"https://api.jcdecaux.com/vls/v3/stations?contract={contract}&apiKey={api_key}"

    #lecture de la reponse de l'API
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())


    velos_meca = 0
    velos_elec = 0
    villes = {}
    nb_stations=len(data)
    for station in data:
        try:
            #somme du nombre de velos mecanique dans toute la ville
            velos_meca += station["totalStands"]["availabilities"]["mechanicalBikes"]
        except KeyError:
            pass             #ne fait rien si la station n'eberge pa de velos mecaniques
            
        try:
            #somme du nombre de velos electrique dans toute la ville
            velos_elec += station["totalStands"]["availabilities"]["electricalBikes"]
        except KeyError:
            pass             #ne fait rien si la station n'eberge pa de velos electriques
            
    
    #parts de velos mécaniques et électriques
    total_velos = velos_meca + velos_elec
    try:
        percentage_meca = round(100 * velos_meca / (total_velos), 2)
        percentage_elec = round(100 * velos_elec / (total_velos), 2)
    except ZeroDivisionError:
        percentage_meca = 0       #affichera 0% si il n'y a pas de velos dans la ville
        percentage_elec = 0
    
    # Afficher les résultats
    print(f"Total number of bikes in : {total_velos}")
    print(f"Pourcentage de vélos mécaniques : {percentage_meca}%")
    print(f"Pourcentage de vélos électriques : {percentage_elec}%")
    print(f"Nombre de stations : {nb_stations}")

    return percentage_meca,percentage_elec

def main():
    villes = cities()
    choice=1
    while choice!=0:
        print("1. Afficher les parts de vélos mécaniques et électriques pour une ville")                              #menu des choix
        print("2. Afficher les parts de vélos mécaniques et électriques pour toutes les villes")
        print("3. Afficher les n villes possédant le plus de velos et leurs pourcentages")
        print("4. Afficher les parts de vélos mécaniques et électriques pour toutes les villes dans un fichier")
        print("0. Quitter")

        choice = int(input("Votre choix : "))
        if choice==1:                            #affiche les stats d'un ville
            ville = input("Ville : ")
            if ville in villes:                                                                   # (blindage) recherche dans les villes reférencées si la ville demandée existe
                print(f"Pourcentage de vélos mécaniques et électriques à {ville.capitalize()}:")
                percentage(ville)
                print()
            else:
                print("Ville inconnue")
        elif choice==2:                            #affiche les stats de toutes les villes

            for ville in villes:
                print(f"Pourcentage de vélos mécaniques et électriques à {ville.capitalize()}:")
                percentage(villes[ville])
                print()

        elif choice==3:                                     #affiche les stats des n premières villes
            nb_villes = int(input("Nombre de villes : "))
            villes = cities()                                #recupère la listes de toutes les villes
            for ville in villes:
                villes[ville] = veloCount(ville)                  #associe le nombre de velos total de la ville a chaque ville 
            sorted_villes = sorted(villes.items(), key=lambda x: x[1], reverse=True)         #tri selon ordre décroissant du nombre de velos
            for ville, count in sorted_villes[:nb_villes]:                                  #affiche les n premières villes
                print(f"{ville}: {count} velos")
                percentage(ville)
                print()
            ''' la sommes des velos electriques et mecaniques "availables" et parfois superieure au nombre total de velos aussi disponibles
             je ne sait pas si j'ai mal compris les données ou si cela viens du fichier, j'ai donc choisi d'afficher les deux,
               le classment se faisant uniquement sur le nombre total  '''
        elif choice==4:
            with open("velos.txt","w") as file:                          #crée un fichier "velos.txt" et y entre le résultat de l'option 2 (les stats pour toutes les villes)
                for ville in villes:
                    file.write(f"Pourcentage de vélos mécaniques et électriques à {ville.capitalize()}:")
                    file.write(str(percentage(ville)))
                    file.write("\n")

        elif choice==0:                             #sortie du programme
            print("Au revoir")
        else:                                  # (blindage) mauvais choix retour au menu principal
            print("Choix invalide")


main()





