import random
moi=50
ennemi=50
moi_potion=3

while True:
    choix= input("Souhaitez-vous attaquer (1) ou boire une potion (2)")
    if choix !="1" and choix !="2":
        print("entrer soit 1 ou 2")
    elif choix.isdigit():
        if choix == "1":
            perte =random.randint(5, 11)
            ennemi -= perte
            print(f" L'ennemi a perdu {perte} points de vie, il a desormais {ennemi} points")
        elif choix =="2":
            gain =random.randint(15, 50)
            moi += gain
            moi_potion -=1
            print(f" Vous avez gangez {gain} points de vie, vous avez {moi} points au total, et il vous reste {moi_potion} potion(s)")
        print("L'ennemi va attaquer")
        perte2= random.randint(5, 16)
        moi -= perte2
        print(f" Vous avez perdu {perte2} points de vie, il vous reste desormais {moi} points")
        print("-----------------------------------------------------------------")
        if moi<=0:
            print("l'ennemi a gagner, vous avez perdu")
            break
        elif ennemi<=0:
            print("vous avez gagné")
            break
    else:
        print("entrer un chiffre")
