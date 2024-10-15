6- Modéliser des RDV médicaux comme sur le site DOCTOLIB


On va utiliser le langage OBJET pour modéliser un petit site qui prend des RDV comme DOCTOLIB
On veut créer un site qui permet à un patient de prendre RDV chez un médecin en ligne.
Supposons que je sois un patient qui cherche un médecin pour une date future.
Donc on sent qu’on va avoir besoin d'une classe Patient et d’une classe Medecin.
Ensuite on va se demander:
- quelles informations peut-on demander à un patient et à un médecin ?
Ces informations seront appelées attributs en langage objet.
- quelles actions peut faire un Patient ? et un Médecin ?

Ces actions seront appelées méthodes en langage objet.


On arrive facilement à écrire les 2 classes suivantes

Classe Patient:
| les attributs      | les méthodes         |
|--------------------|----------------------|
| prenom             | prendre_RDV()        |
| nom                | se_presenter()       |
| adresse            | payer_consultation() |
| date_naissance     |                      |
| sexe               |                      |
| num_SS             |                      |


Classe Medecin:
| les attributs       | les méthodes |
|---------------------|--------------|
| prenom              | consulter()  |
| nom                 | prescrire()  |
| adresse             | facturer()   |
| date_naissance      |              |
| sexe                |              |
| specialite          |              |


On voit que ces 2 classes Patient et Medecin ne suffisent pas à gérer des RDV médicaux.

Pour faire le lien entre ces 2 classes, on doit ajouter une classe RDV.

Classe RDV:
| les attributs | les méthodes  |
|---------------|---------------|
| date_RDV      | fixer_RDV()   |
| Heure_debut   | annuler_RDV() |
| heure_fin     |               |
| salle_bureau  |               |


Voilà notre 1ère vue d’ensemble du modèle

|           | Classe Patient       | Classe Medecin | Classe RDV    |
|-----------|----------------------|----------------|---------------|
| Attributs | prenom               | prenom         | date_RDV      |
|           | nom                  | nom            | heure_debut   |
|           | adresse              | adresse        | heure_fin     |
|           | date_naissance       | date_naissance | salle_bureau  |
|           | sexe                 | sexe           |               |
|           | num_SS               | specialite     |               |
| Méthodes  | prendre_RDV()        | consulter()    | fixer_RDV()   |
|           | se_presenter()       | prescrire()    | annuler_RDV() |
|           | payer_consultation() | facturer()     |               |

1er constat :

En créant la classe RDV, on se rend compte qu'on a besoin d'un identifiant unique pour identifier
précisément le médecin et le patient du RDV.

Donc on retourne sur nos classes Patient et Medecin et on ajoute à notre modèle les identifiants suivants :

  idMedecin
  
  idPatient
  
  idRDV


Nous arrivons à cette 2ème version du modèle

|           | Classe Patient       | Classe Medecin | Classe RDV    |
|-----------|----------------------|----------------|---------------|
| Attributs | id_patient           | id_medecin     | id_RDV        |
|           | prenom               | prenom         | id_medecin    |
|           | nom                  | nom            | id_patient    |
|           | adresse              | adresse        | date_RDV      |
|           | date_naissance       | date_naissance | heure_debut   |
|           | sexe                 | sexe           | heure_fin     |
|           | num_SS               | specialite     | salle_bureau  |
| Méthodes  | prendre_RDV()        | consulter()    | fixer_RDV()   |
|           | se_presenter()       | prescrire()    | annuler_RDV() |
|           | payer_consultation() | facturer()     |               |

2ème constat :

En prenant du recul, on remarque qu'il y a des informations communes aux classes Patient et Medecin.

  prenom
  
  nom
  
  adresse
  
  date_naissance
  
  sexe

Comme la Programmation Orientée Objet a été créée pour nous simplifier la vie, on pourrait donc créer une
classe mère, disons la classe Personne, pour regrouper ces informations et les mutualiser.
Voici la définition de la nouvelle classe Personne, qui sera la classe mère de Patient et Medecin

|           | Classe Personne      |
|-----------|----------------------|
| Attributs | prenom               |
|           | nom                  |
|           | adresse              |
|           | date_naissance       |
|           | sexe                 |
| Méthodes  | creer()              |
|           | effacer()            |

Notre modèle est plus complet et devient :

| Classe Personne      |
|----------------------|
| prenom               |
| nom                  |
| adresse              |
| date_naissance       |
| sexe                 |
|----------------------|
| creer()              |
| effacer()            |


Les 2 classes filles Patient et Medecin sont simplifiées en héritant de Personne et deviennent donc :

|           | Classe Patient(Personne) | Classe Medecin(Personne) | Classe RDV    |
|-----------|--------------------------|--------------------------|---------------|
| Attributs | id_patient               | id_medecin               | id_RDV        |
|           | num_SS                   | specialite               | id_medecin    |
|           |                          |                          | id_patient    |
|           |                          |                          | date_RDV      |
|           |                          |                          | heure_debut   |
|           |                          |                          | heure_fin     |
|           |                          |                          | salle_bureau  |
| Méthodes  | prendre_RDV()            | consulter()              | fixer_RDV()   |
|           | se_presenter()           | prescrire()              | annuler_RDV() |
|           | payer_consultation()     | facturer()               |               |

Quand on est content de notre modèle de données, qu’on peut répondre aux principales questions des métiers,
on peut commencer à programmer le modèle.


EXERCICE A COMMENCER A LA MAISON

1- Créer le fichier vide ma_lib_RDV.py sur VSC


2- Créer en PYTHON les 4 classes définies ci-dessus :

  Personne
  
  Patient classe fille de Personne
  
  Medecin classe fille de Personne
  
  RDV


3- Programmer les attributs et les méthodes des 4 classes précédentes


4- j’ai créé un fichier JSON qui contient déjà des données de base :

  2 Medecins
  
  1 patient
  
  2 RDV du patient chez 2 médecins différents.

  
Comme on l’a fait avec le fichier c:/amis.txt, on va lire le fichier JSON appelé mes_rdv.json et s’en servir pour
lire et stocker des informations.

Je vous donne la syntaxe du fichier en entrée appelé mes_rdv.json à utiliser pour l’exercice


Avant de programmer en PYTHON les 4 classes d’objets définies précédemment, quelques remarques :

On a mis la méthode prendre_RDV() dans la Classe Patient.

Après réflexion, ça fait doublon avec fixer_RDV() de la Classe RDV

Donc, avant de coder dans Python, on va supprimer la méthode prendre_RDV() dans Patient

Par contre, on va ajouter pour toutes les 4 classes la méthode afficher() et on ne codera que cette méthode
afficher() pour chacune des 4 classes :

2 raisons à cela :

1- faire un print() est le plus simple à coder pour débuter en POO

2- ca nous fait comprendre le “polymorphisme, çàd, avoir une même nom de méthode pour plusieurs comportements différents

3- On pourra tester et exécuter le code et avoir des résultats rapides.


|           | Classe Personne | Classe Patient(Personne) | Classe Medecin(Personne) | Classe RDV    |
|-----------|-----------------|--------------------------|--------------------------|---------------|
| Attributs | prenom          | id_patient               | id_medecin               | id_RDV        |
|           | nom             | num_SS                   | specialite               | id_medecin    |
|           | adresse         |                          |                          | id_patient    |
|           | date_naissance  |                          |                          | date_RDV      |
|           | sexe            |                          |                          | heure_debut   |
|           |                 |                          |                          | heure_fin     |
|           |                 |                          |                          | salle_bureau  |
| Méthodes  | afficher()      | afficher()               | afficher()               | afficher()    |
|           | creer()         | ~~prendre_RDV()~~        | consulter()              | fixer_RDV()   |
|           | effacer()       | se_presenter()           | prescrire()              | annuler_RDV() |
|           |                 | payer_consultation()     | facturer()               |               |

