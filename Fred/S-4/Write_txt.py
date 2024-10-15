
def ecrire(chemin) : 
    new_name = input("Saisir le prénom : ")
    new_age = input("Saisir l'age : ")

    with open(chemin, 'r+') as fichier:
        fichier.seek(0, 2)           # Se placer à la fin du fichier
        fichier.write(f"\n{new_name};{new_age}")        # Ecrire la nouvelle entrée
        fichier.seek(0)             # Se placer au début du fichier
        print(fichier.read())

ecrire("c:/temp/amis.txt")