import json

chemin ="/Users/elodiemariton/code/elodiemar/testpython/test.json"

with open(chemin, "w") as f: # "a" append ajoute a la fin x'est mieux que w qui ecrase
    #json.dump("bonjour", f)
    json.dump(list(range(10)), f, indent=4)

#lire avec json

with open(chemin, "r") as f:
    liste = json.load(f)
    print(liste)
