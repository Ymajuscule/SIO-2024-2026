def calc_placement():
    capital = float(input("Saisir le capital de départ : "))
    duree = int(input("Saisir la durée : "))
    taux = float(input("Saisir le taux : "))

    n_cap = []
    result = capital

    for i in range(duree):
        result *= (1 + taux)
        n_cap.append(round(result, 2))
        print(f"Le capital pour l'année {i+1} est {round(result,2)}")
    print()
    print(f"La liste : {n_cap}")

print("------------ calc_placement ------------")
calc_placement()
print("------------------ fin ------------------")
