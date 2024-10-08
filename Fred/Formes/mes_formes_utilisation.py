from mes_formes import Carre, Cercle

# Déclarations
mon_carre = Carre("Rouge", (200, 200), 60)
mon_cercle = Cercle("Bleu", (100, 100), 50)

# Affichage des informations du Carré
print("-------------------- Carré --------------------")
mon_carre.afficher()
print("L'aire du carré est :", mon_carre.calculer_aire())
print("Le périmetre du carré est :", mon_carre.calculer_perimetre())

# Affichage des informations du Cercle
print("-------------------- Cercle --------------------")
mon_cercle.afficher()
print("L'aire du cercle est :", mon_cercle.calculer_aire())
print("Le périmetre du cercle est :", mon_cercle.calculer_perimetre())
print("------------------------------------------------")

print("{:<10} | {:<10} | {}".format("Attribut", "Carré", "Cercle"))
print("{:<10} | {:<10} | {}".format("Aire", mon_carre.calculer_aire(), round(mon_cercle.calculer_aire(),0)))
print("{:<10} | {:<10} | {}".format("Perimètre", mon_carre.calculer_perimetre(), round(mon_cercle.calculer_perimetre(),0)))

print("--------------------- Fin ---------------------")
