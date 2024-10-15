from turtle import *
from time import sleep

def Attente():
    sleep(2)

def Carre(): # Dessin d'un carré
    for i in range(4):
        forward(100)        # Dessine une droite de 100 px
        left(90)            # Tourne à gauche de 90°
    Attente()

def Hexagonne():            # Dessine un hexagone
    for i in range(6):
        forward(100)        # Dessine une droite de 100 px
        left(60)            # Tourne à gauche de 60°
    Attente()

def Spire():                # Dessine une spire 
    pas = 5
    for i in range(60):
        forward(pas)
        left(60)
        pas += 5
    Attente()

def Cercle():
    circle(60)
    Attente()

def Cercle1():
    for i in range(360):
        forward(2)
        left(1)
    Attente()


Carre()
clear()
Hexagonne()
clear()
Spire()
clear()
Cercle()
clear()
Cercle1()