chemin ="/Users/elodiemariton/code/elodiemar/testpython/list.py"


#lire un fichier
with open(chemin, "r") as f: #methode with evite davoir a femrer le fichier soit meme
    contenu = repr(f.read()) # repr pour ne pas avoir les retours à la ligne pratique pour mes longues phrases
    print(contenu)

#ecrire dans un fichier
with open(chemin, "a") as f: # append ajoute a la fin x'est mieux que w qui ecrase
    f.write("bonjour")
