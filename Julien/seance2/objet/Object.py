import math

class Figure:
    def __init__(self, couleur,position):
        self.couleur = couleur
        self.postion = position

    def deplacer(self, dx, dy):
        self.postion = (self.postion[0] + dx, self.postion[1] + dy)
    
    def afficher(self):
        print(f'figure de couleur {self.couleur} situé en  {self.postion}')


class Carre(Figure):
    def __init__(self, couleur, position, cote):
        super().__init__(couleur,position)
        self.cote = cote

    def calculer_aire(self):
        return self.cote * self.cote
    
    def calculer_perimetre(self):
        return 4 * self.cote
    

class Cercle(Figure):
    def __init__(self, couleur, position,rayon):
        super().__init__(couleur, position)
        self.rayon = rayon

    def calculer_air(self):
        return math.pi * self.rayon
    
    def calculer_perimetre(self):
        return 2 * math.pi * self.rayon