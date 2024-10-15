my_list = ["1 a", "2 b", "3 c"]

index = int(input("Entrer un index : "))

try:
    element = my_list[index]
    print(element)
except IndexError:
    print("L'index est invalide.")