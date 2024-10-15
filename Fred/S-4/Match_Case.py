import datetime

date_day = datetime.date.today()

day = date_day.weekday()

print("Aujourd'hui on est", end=" ")

match day:
    case 0:
        print("Lundi")

    case 1:
        print("Mardi")

    case 2:
        print("Mercredi")

    case 3:
        print("Jeudi")

    case 4:
        print("Vendredi")

    case 5:
        print("Samedi")
        
    case 6:
        print("Dimanche")
    
 #   case _ :
    case default:
        print("Le jour de la semaine n'existe pas !")
        
