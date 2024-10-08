import math

class Figure :
    def __init__(self, couleur, position):
        self.couleur = couleur
        self.position = position

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def afficher(self):
        print(f"Figure de couleurs {self.couleur} situé en {self.position}")


class Carre(Figure):
    def __init__(self, couleur, position, cote):
        super().__init__(couleur, position)

        self.cote = cote

    def calculer_aire(self):
        return self.cote * self.cote
        
    def calculer_perimetre(self):
        return 4 * self.cote


class Cercle(Figure):
    def __init__(self, couleur, position, rayon):
        super().__init__(couleur, position)
        self.rayon = rayon

    def calculer_aire(self):
        return math.pi * self.rayon ** 2
        
    def calculer_perimetre(self):
        return 2 * math.pi * self.rayon
    
