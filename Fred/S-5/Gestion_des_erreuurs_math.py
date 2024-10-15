try:
    nombre = int(input("Entrer un nombre : "))
    result = 10 / nombre
    print(result)

except ValueError:
    print("Vous n'avez pas entré un nombre valide !")

except ZeroDivisionError:
    print("Division par zéro impossible !")