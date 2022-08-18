import os
import json
CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "liste.json")

MENU = """ Choisissez parmis les options suivantes :
1: Ajouter un élement à la liste
2: Retirer un élement à la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
"""
MENU_CHOICES = ["1", "2", "3", "4", "5"]

if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as f:
        LISTE = json.load(f)
else:
    LISTE = []


while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")
    if user_choice == "1":
        item= input("entrer un ingredient à ajouter  : ")
        LISTE.append(item)
        with open("liste.json", "w") as f:
            json.dump(LISTE, f)
        print(f"L'élement {item} a bien été ajouté")
    elif user_choice =="2":
        item= input("entrer un ingredient à supprimer5: ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élement {item} a bien été supprimé")
        else:
            print("l'élement n'est pas dans la liste")
    elif user_choice =="3":
        if LISTE:
            print(" Voici le contenu de votre liste de course : ")
            for i, item in enumerate(LISTE,1):
                print(f" {i} : {item}")
        else:
            print("Il n'y a rien dans votre liste")
    elif user_choice =="4":
        LISTE.clear()
    elif user_choice == "5":
        with open(LISTE_PATH, "w") as f:
            json.dump(LISTE, f, indent=4)
        print("À bientôt !")
        sys.exit()
