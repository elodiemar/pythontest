mdp = input("entrez votre mot de passe, 8 caractère minimum : ")
mdp_vide ="Votre mot de passe est vide"
mdp_court= "votre mot de passe est trop court"
mdp_nombre = "Votre mot de passe contient uniquement des nombres"
mdp_ok ="BRAVO"

if mdp == "":
    print(mdp_vide.upper())
elif len(mdp) < 8:
    print(mdp_court.capitalize())
elif mdp.isdigit():
    print(mdp_nombre.title())
else:
    print(mdp_ok)
