def Lenght_Sentence(sentence):
    longwords = 0
    nbelement = 0
    for punctuation in "!?',;.":
        sentence = sentence.replace(punctuation, ' ')
        words = sentence.split()
    return sum(len(word) for word in words)/len(words)



print(Lenght_Sentence("Le blog 'ledatascientist' est le blog français de référence en Data Science. Nous allons maintenant écrire une fonction qui calcule la longueur moyenne des mots de notre texte."))
