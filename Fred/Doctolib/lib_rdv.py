class Personne:
    def __init__(self, prenom, nom, adresse, date_naissance, sexe):
        self.prenom = prenom
        self.nom = nom
        self.adresse = adresse
        self.date_naissance = date_naissance
        self.sexe = sexe
    def afficher(self):
        print(f"Vous êtes : {self.prenom} {self.nom}, \n né(e) le {self.date_naissance}, de sexe {self.sexe} \n habitant au {self.adresse}")

class Patient(Personne):
    def __init__(self, id_patient, prenom, nom, adresse, date_naissance, sexe, num_SS):
        super().__init__(prenom, nom, adresse, date_naissance, sexe)
        self.id_patient = id_patient
        self.num_SS = num_SS
    def afficher(self):
        super().afficher() # Appelle la méthode afficher() de la classe parente
        print(f"ID Patient : {self.id_patient}")
        print(f"Num. Sécur. Soc. : {self.num_SS}")

class Medecin(Personne):
    def __init__(self, id_medecin, prenom, nom, adresse, date_naissance, sexe, specialite):
        super().__init__(prenom, nom, adresse, date_naissance, sexe)
        self.id_medecin = id_medecin
        self.specialite = specialite
    def afficher(self):
        super().afficher() # Appelle la méthode afficher() de la classe parente
        print(f"ID Médecin : {self.id_medecin} de spécialité : {self.specialite}")

class RDV:
    def __init__(self, id_rdv, id_patient, id_medecin, date_rdv, heure_debut, heure_fin, motif):
        self.id_rdv = id_rdv
        self.patient = id_patient
        self.medecin = id_medecin
        self.date_rdv = date_rdv
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.motif = motif
    def afficher(self):
        print(f"ID RDV : {self.id_rdv} avec ID Patient : {self.id_patient} \n vu par ID Médecin {self.id_medecin}, le {self.date_rdv} \n entre {self.heure_debut} et {self.heure_fin} avec motif : {self.motif}")