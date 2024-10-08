values = []
sentence = ['quel est votre capital : ','quelle durée : ','quel taux : ']
all_years = []

def calc_placement():
    
    for i in range(3):
        cap = float(input(sentence[i]))
        values.append(cap)
    print(f'\n-------------Taux sur {values[1]} années-------------')
    print(f'Pour un invesstisement de {values[0]:.0f}, une durée de {values[1]} et un taux à {values[2]}, le résultat est donc de : {values[0] * (1 + values[2]) ** values[1]}\n')
    print('\n-------------Chaque Année-------------')
    for i in range(1,11):
        all_years.append(values[0] * (1 + values[2]) ** i)
        print(f' année {i} : {values[0] * (1 + values[2]) ** i}')
    
    



calc_placement()