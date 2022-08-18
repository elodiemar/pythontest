nbr1 = nbr2 =""
while not (nbr1.isdigit() and nbr2.isdigit()):
    nbr1 = input("Entrer un chiffre : ")
    nbr2= input("Entrer un chiffre : ")
    print("Veuillez entrer deux chiffres valides")
add= int(nbr1) + int(nbr2)
print(f" la somme de {nbr1} et {nbr2} est egale à {add}")
