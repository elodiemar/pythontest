from math import sqrt # Importer la fonction de racine carrée

def is_Pythagorean_triplet(list_):
    # Vérifier que notre liste est de longueur appropriée avant tout traitement
    if len(list_) < 3:
        triplet = "Il faudrait réessayer avec une liste d'entiers positifs de longueur minimum 3."

    # Notre liste est de longueur minimum 3
    else:
        n = len(list_) # Longueur de notre liste
        triplet = [] # Liste de tuples à retourner
        m = 0 # Index du premier élément de la liste

        # Parcourons notre liste et recherchons les triplets Pythagoriciens
        for i in range(n - 2):
            for k in range(m + 1, n):
                for j in range(k + 1, n - 1):
                    # Calculons le carré de chaque élément de la liste
                    x = list_[i] * list_[i]
                    y = list_[j] * list_[j]
                    z = list_[k] * list_[k]
                    if x == y + z or y == x + z or z == x + y:
                        triplet.append((int(sqrt(x)),
                                        int(sqrt(y)),
                                        int(sqrt(z))))

    # Nous retournons la liste des triplets Pythagoriciens
    return triplet # Notre liste peut être vide si nous en trouvons pas

# Application de notre fonction
print(is_Pythagorean_triplet([0, 3, 4, 5, 2, 4, 6]))
