import random

def lancer_de():
    return random.randint(1, 6)

def lancer_jusqu_a_6():
    lancers = 0
    resultat = 0

    print("Lancement du dé jusqu'à obtenir un 6...\n")
    
    while resultat != 6:
        resultat = lancer_de()
        lancers += 1
        print(f"Lancer {lancers}: {resultat}")
    
    print(f"\nUn 6 a été obtenu après {lancers} lancers.")

lancer_jusqu_a_6()