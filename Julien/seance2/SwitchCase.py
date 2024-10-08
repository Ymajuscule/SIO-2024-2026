import datetime


day_of_week = datetime.date.today().weekday()

print("ajourd'hui est un", end= " ")


match day_of_week:
    case 0:
        print('lundi')
    case 1:
        print('mardi')
    case 2:
        print('mercredi')
    case 3:
        print('jeudi')
    case 4:
        print('vendredi')
    case 5:
        print('samedi')
    case 6:
        print('dimanche')
    case default:
        print('Erreur dans le jour')