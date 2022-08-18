# boucles et conditions

a=[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
b=range(10)
nbr_positif =[i for i in a if i>=0]
nbr_neg =[i for i in a if i<0]
nbr_twice =[i*2 for i in a if i>0]
nbr_pair =[i for i in a if i%2==0]

nbr_pair_reverse =[i if i%2==0 else -i for i in b ]
print(nbr_positif)
print(nbr_neg)
print(nbr_twice)
print(nbr_pair)
print(nbr_pair_reverse)

# boucle While
#ex1

i=0
while i <10:
    print(f"Utilisateurs : {i+1}")
    i+=1

for i in range(10):
    print(f"Utilisateurs : {i+1}")


# chaine de caractère

#afficher à l'envers
#solution 1

welcome1 = "Hello World"[::-1]
print(welcome1)

#solution 2
welcome2 ="Hello Word"
# print(list(reversed(welcome))) si on ne met pas liste on a une message <reversed object at 0x100c53ee0>
for letter in reversed(welcome2):
    print(letter)

#while
answer= "o"
while answer == "o":
    print("voulez vous continuer")
