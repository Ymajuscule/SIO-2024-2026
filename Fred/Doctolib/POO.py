import json
import lib_rdv as libRdv

fichier = "c:/temp/mes_rdv.json"
donnees = libRdv.lire_donnees(fichier)

if donnees:
    print("----------- Medecin -----------")
    for medecin in donnees['medecin']:
        print(f"Médecin {medecin['specialite']} : {medecin['prenom']} {medecin['nom']}")

    print("\n---------- Patient ----------")
    for patient in donnees['patient']:
        print(f"Patient {patient['num_SS']} : {patient['prenom']} {patient['nom']}")

    print("\n------------ RDV ------------")
    for rdv in donnees['rdv']:
        print(f"RDV n° {rdv['id_rdv']} du patient {rdv['id_patient']}")

    print("\n--------- RDV traduit ---------")
    for rdv in donnees['rdv']:
        for patient in donnees['patient']:
            if patient['id_patient'] == rdv['id_patient']:
                patient_nom = f"{patient['prenom']} {patient['nom']}"

        for medecin in donnees['medecin']:
            if medecin['id_medecin'] == rdv['id_medecin']:
                medecin_nom = f"{medecin['prenom']} {medecin['nom']}"
        
        print(f"RDV n° {rdv['id_rdv']} du patient {patient_nom} vu par {medecin_nom}")
    
    print("\n------------ Fin ------------")