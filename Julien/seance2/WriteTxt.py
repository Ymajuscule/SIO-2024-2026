def Main():
    prenom = str(input('Veuillez donner votre prénom'))
    age = str(input('Veuillez donner votre age'))

    with open('C:/Users/jsail/Desktop/Cours/python/Main.txt','a') as fichier:
        fichier.write(f'{prenom};{age}\n')


    with open('C:/Users/jsail/Desktop/Cours/python/Main.txt', 'r') as fichier:
        for ligne in fichier:
            print(ligne)


Main()