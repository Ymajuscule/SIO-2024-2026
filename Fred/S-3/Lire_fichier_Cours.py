def lire_fichier(fic):
    amis = {}
    with open(fic, 'r') as fichiers:
        for ligne in fichiers:
            prenom, age = ligne.strip().split(';')
            if prenom != 'prenom':
                amis[prenom] = age
                print(f"{prenom} à {age} ans")
    print(amis)

lire_fichier("c:/temp/amis.txt")
