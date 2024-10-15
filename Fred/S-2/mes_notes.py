from statistics import mean

# Calcul des notes
mes_notes = [15, 8, 12, 11.5]

def Calcul_notes(list):
    # Compter les notes
    print("Il y a ", len(list), " notes")

    # Afficher la note mini
    print("La note minimale est ", min(list))

    # Afficher la note maxi
    print("La note maximale est ", max(list))

    # Calculer la somme des notes
    print("La somme des note est ", sum(list))

    # Caluler la moyenne
    somme = sum(list)
    nb_notes = len(list)
    print("La moyenne des notes est ", somme/nb_notes)

def Calcul_Stat(list_stat):
    average = mean(list_stat)
    print("La moyenne des notes est ", average)

Calcul_notes(mes_notes)
Calcul_Stat(mes_notes)