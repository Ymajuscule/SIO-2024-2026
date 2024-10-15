from random import *

mon_de = 0
nb_lancer = 0
list_lancers = []

while (mon_de != 6):
    mon_de = randint(1, 6)
    nb_lancer += 1
    list_lancers.append(mon_de)

print("Nombre de lancés", nb_lancer)
print("Les valeur eu sont", list_lancers)
