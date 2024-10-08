amis = {}

with open('C:/Users/jsail/Desktop/Cours/python/Main.txt', 'r') as fichier:
    for ligne in fichier:
        prenom, age = ligne.strip().split(';')
        if prenom != 'prenom':
            amis[prenom] = age



for i in amis:
    print(f'{i} à {amis[i]}')
print(amis)
