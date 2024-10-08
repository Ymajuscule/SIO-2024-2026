from Object import Carre,Cercle

mon_carre = Carre('rouge',(200,200),60)
mon_cercle = Cercle('bleu',(100,100),50)


mon_carre.afficher()
print("l'aire du carré est :", mon_carre.calculer_aire())
print("l'aire du carré est :", mon_carre.calculer_perimetre)


mon_cercle.afficher()
print("l'aire du carré est :", mon_cercle.calculer_air())
print("l'aire du carré est :", mon_cercle.calculer_perimetre())