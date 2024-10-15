def demander_nom():
    nom = input("Saisir ton nom : ").upper()
    prenom = input("Saisir ton prénom : ").capitalize()

    print(f "Bonjour {nom} {prenom}")

demander_nom()