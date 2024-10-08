mes_notes = [15,8,12,11.5]

def Main(list):
    total = sum(list) / len(list)
    print("la moyenne est de",total)
    print("le nombre minimum", min(list))
    print(max(list))

Main(mes_notes)