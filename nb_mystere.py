import random

nbr= random.randint(0, 101)
attempt=0

while attempt < 5:
    guess_nbr = input("Devinez le nombre : ")
    if guess_nbr.isdigit():
        attempt+=1
        if attempt >=5 :
            print(f"Vous avez perdu le nombre était {nbr}")
        elif int(guess_nbr) == nbr:
            print(f"vous avez gagné en {attempt} coups")
            break
        elif int(guess_nbr) > nbr:
            print(f"le chiffre est plus petit, il vous reste {5- attempt} tentatives")
        else:
            print(f"le chiffre est plus grand, il vous reste {5- attempt} tentatives")
    else:
        print("Veuille entrer NOMBRE ")
