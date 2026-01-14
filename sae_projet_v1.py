import csv
import matplotlib.pyplot as plt

Donnees=[]
with open('donnees_hebdo.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
#        print(','.join(row))
        Donnees.append(row)
#print(Donnees)


#Donnees de consommation corrigee en semaines pour chaque année (2025, 2024, 2023, 2022, 2021, 2020)

semaine_2025=[]
for element in Donnees: 
    if element[0] == 'semaine' and element[4] == '2025' and element[6] != "NA":
        semaine_2025.append(float(element[6].replace(",", ".")))  # Convertir en float

semaine_2024=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2024' and element[6] != "NA":
        semaine_2024.append(float(element[6].replace(",", ".")))

semaine_2023=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2023' and element[6] != "NA":
        semaine_2023.append(float(element[6].replace(",", ".")))

semaine_2022=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2022' and element[6] != "NA":
        semaine_2022.append(float(element[6].replace(",", ".")))

semaine_2021=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2021' and element[6] != "NA":
        semaine_2021.append(float(element[6].replace(",", ".")))

semaine_2020=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2020' and element[6] != "NA":
        semaine_2020.append(float(element[6].replace(",", ".")))


plt.plot(range(1, len(semaine_2025)+1), semaine_2025, marker="o", label="2025")
#plt.plot(range(1, len(semaine_2024)+1), semaine_2024, marker="o", label="2024")
#plt.plot(range(1, len(semaine_2023)+1), semaine_2023, marker="o", label="2023")
#plt.plot(range(1, len(semaine_2022)+1), semaine_2022, marker="o", label="2022")
#plt.plot(range(1, len(semaine_2021)+1), semaine_2021, marker="o", label="2021")
#plt.plot(range(1, len(semaine_2020)+1), semaine_2020, marker="o", label="2020")

plt.xlabel("Semaine de l'année")
plt.ylabel("Consommation corrigée")
plt.title("Évolution hebdomadaire de la consommation (2020 - 2025)")
plt.grid(True)
plt.legend()
plt.show()


#Consommation brute 2025 - 2020

# Conso brute 2025
donnees_brute2025 = {}
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2025':
        semaine = element[3]
        conso_brute1 = element[10]
        if conso_brute1 == 'NA':
            valeur = None
        else:
            valeur = float(conso_brute1.replace(",", "."))
        donnees_brute2025[semaine] = valeur
#print(donnees_brute2025)

# conso brute 2024
donnees_brute2024 = {}
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2024':
        semaine = element[3]
        conso_brute2 = element[10]
        if conso_brute2 == 'NA':
            valeur = None
        else:
            valeur = float(conso_brute2.replace(",", "."))
        donnees_brute2024[semaine] = valeur
#print(donnees_brute2024)

# Conso brute 2023
donnees_brute2023 = {}
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2023':
        semaine = element[3]
        conso_brute3 = element[10]
        if conso_brute3 == 'NA':
            valeur = None
        else:
            valeur = float(conso_brute3.replace(",", "."))
        donnees_brute2023[semaine] = valeur
#print(donnees_brute2023)

# Conso brute 2022
donnees_brute2022 = {}
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2022':
        semaine = element[3]
        conso_brute4 = element[10]
        if conso_brute4 == 'NA':
            valeur = None
        else:
            valeur = float(conso_brute4.replace(",", "."))
        donnees_brute2022[semaine] = valeur
#print(donnees_brute2022)

# Conso brute 2021
donnees_brute2021 = {}
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2021':
        semaine = element[3]
        conso_brute5 = element[10]
        if conso_brute5 == 'NA':
            valeur = None
        else:
            valeur = float(conso_brute5.replace(",", "."))
        donnees_brute2021[semaine] = valeur
#print(donnees_brute2021)

#conso brute 2020
donnees_brute2020 = {}
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2020':
        semaine = element[3]
        conso_brute6 = element[10]
        if conso_brute6 == 'NA':
            valeur = None
        else:
            valeur = float(conso_brute6.replace(",", "."))
        donnees_brute2020[semaine] = valeur
#print(donnees_brute2020)


import matplotlib.pyplot as plt

# Regrouper les données brutes dans un seul dictionnaire
donnees_brutes = {
    "2025": donnees_brute2025,
    "2024": donnees_brute2024,
    "2023": donnees_brute2023,
    "2022": donnees_brute2022,
    "2021": donnees_brute2021,
    "2020": donnees_brute2020
}

plt.figure(figsize=(12,6))

for annee, data_brute in donnees_brutes.items():
    semaines = []
    valeurs_valides = []

    for i, val in data_brute.items():
        try:
            semaine_int = int(i)
            if val is not None:
                semaines.append(semaine_int)
                valeurs_valides.append(val)
        except:
            pass

    semaines_valeurs = sorted(zip(semaines, valeurs_valides))
    if semaines_valeurs:
        semaines, valeurs_valides = zip(*semaines_valeurs)
        plt.plot(semaines, valeurs_valides, marker="o", label=annee)

plt.xlabel("Semaine de l'année")
plt.ylabel("Consommation brute")
plt.title("Consommation brute hebdomadaire (2020 - 2025)")
plt.grid(True)
plt.legend()
plt.xticks(range(1, 54, 2))
plt.tight_layout()
plt.show()


#Donnees conso corrigee en fonction des donnees conso brute des semaines

import matplotlib.pyplot as plt

# Regrouper toutes les données corrigées et brutes par année
donnees_corrigees = {
    "2025": semaine_2025,
    "2024": semaine_2024,
    "2023": semaine_2023,
    "2022": semaine_2022,
    "2021": semaine_2021,
    "2020": semaine_2020
}

donnees_brutes = {
    "2025": donnees_brute2025,
    "2024": donnees_brute2024,
    "2023": donnees_brute2023,
    "2022": donnees_brute2022,
    "2021": donnees_brute2021,
    "2020": donnees_brute2020
}

plt.figure(figsize=(14,7))

for annee in ["2025","2024","2023","2022","2021","2020"]: 

    #Courbe pour les données corrigées
    data_corrigee = donnees_corrigees[annee]
    plt.plot(range(1, len(data_corrigee)+1), data_corrigee,marker="x", linestyle='--', label=f"Corrigée {annee}")
    #Courbe pour les données brutes
    data_brute = donnees_brutes[annee] 
    # Trier les semaines 
    semaines_valides2 = []
    valeurs_valides2 = []
    for s, val in data_brute.items():
        try:
            s_int = int(s)
            if val is not None:
                semaines_valides2.append(s_int)
                valeurs_valides2.append(val)
        except:
            pass
    # Trier maintenant par semaine
    if semaines_valides2:
        semaines_valides2, valeurs_valides2 = zip(*sorted(zip(semaines_valides2, valeurs_valides2)))
        plt.plot(semaines_valides2, valeurs_valides2,marker="o", linestyle='-', label=f"Brute {annee}")

#Affichage de la courbe
plt.xlabel("Semaine de l'année")
plt.ylabel("Consommation")
plt.title("Comparaison consommation brute vs corrigée (2020 - 2025)")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05,1), loc='upper left')
plt.xticks(range(1, 54, 2))
plt.tight_layout()
plt.show()


#MOYENNE CONSO CORRIGEE ET BRUTES POUR CHAQUE ANNEE
import matplotlib.pyplot as plt
import numpy as np

annees = [2025, 2024, 2023, 2022, 2021, 2020] # Liste des années 
donnees_corrigeee = [semaine_2025, semaine_2024, semaine_2023, semaine_2022, semaine_2021, semaine_2020]
donnees_brutees = [donnees_brute2025, donnees_brute2024, donnees_brute2023, donnees_brute2022, donnees_brute2021, donnees_brute2020]

moyenne_corrigees_par_annee = [] # On va calculé la moyenne corrigée pour chaque année
moyenne_brutes_par_annee = [] # On va calculé la moyenne brute pour chaque année

for i in range(len(annees)):

    # La Moyenne corrigée
    data_corr = donnees_corrigeee[i]
    moyenne_corr = []
    for k in range(len(data_corr)):
        valeur = data_corr[k]
        moyenne_corr.append(valeur if valeur is not None else np.nan) #np.nan ignore les valeurs manquants
    moyenne_corrigees_par_annee.append(moyenne_corr)
    
    #Moyenne brute
    data_brutees = donnees_brutees[i]
    nb_semainees = max(len(data_brutees), 1)
    moyenne_brut = []
    for m in range(1, nb_semainees + 1):
        total = 0
        compteur = 0
        for d in [data_brutees]: #dans un dictionnaire
            if str(m) in d:
                val = d[str(m)]
                if val is not None:
                    total += val
                    compteur += 1
        moyenne_brut.append(total / compteur if compteur > 0 else np.nan) #eviter les valeurs None, donc manquants
    moyenne_brutes_par_annee.append(moyenne_brut)

#Affichage graphique par année
for i, annee in enumerate(annees):
    plt.figure(figsize=(10,5)) #définit la taille de la figure (Largeur, hauteur)
    #Semaines pour chaque courbe
    semaines_corrigee = list(range(1, len(moyenne_corrigees_par_annee[i]) + 1))
    semaines_brutee = list(range(1, len(moyenne_brutes_par_annee[i]) + 1))
    plt.plot(semaines_corrigee, moyenne_corrigees_par_annee[i], marker='x', linestyle='--', color='blue', label="Moyenne corrigée")
    plt.plot(semaines_brutee, moyenne_brutes_par_annee[i], marker='o', linestyle='-', color='red', label="Moyenne brute")
    plt.xlabel("Semaine de l'année")
    plt.ylabel("Consommation")
    plt.title(f"Consommation moyenne brute vs corrigée {annee}")
    plt.grid(True)
    plt.legend()
    plt.xticks(range(1, 54, 2))
    plt.tight_layout()
    plt.show()


#La moyenne des consommations corrigées et brutes
import matplotlib.pyplot as plt
import numpy as np

#La Moyenne corrigée
donnees_corrigees = [semaine_2025, semaine_2024, semaine_2023, semaine_2022, semaine_2021, semaine_2020]
nb_semaines1 = max(len(s) for s in donnees_corrigees)

moyenne_corrigee = []
for i in range(nb_semaines1):
    valeurs_semaine = []
    for data in donnees_corrigees:
        if i < len(data):
            valeurs_semaine.append(data[i])
    if valeurs_semaine:
        moyenne_corrigee.append(np.mean(valeurs_semaine))
    else:
        moyenne_corrigee.append(np.nan)  # <-- utiliser np.nan
#print(moyenne_corrigee)

#La Moyenne brute
donnees_brutes = [donnees_brute2025, donnees_brute2024, donnees_brute2023, donnees_brute2022, donnees_brute2021, donnees_brute2020]
nb_semaines2 = max(len(data) for data in donnees_brutes)

moyenne_brute = []
for s in range(1, nb_semaines2 + 1):  # on commence à 1 pour correspondre aux clés
    total = 0
    compteur = 0
    for data in donnees_brutes:
        if str(s) in data:
            val = data[str(s)]
            if val is not None:
                total += val
                compteur += 1
    if compteur > 0:
        moyenne_brute.append(total / compteur)
    else:
        moyenne_brute.append(np.nan)
#print(moyenne_brute)

plt.figure(figsize=(12,6))
plt.plot(range(1, len(moyenne_corrigee)+1), moyenne_corrigee, marker='x', linestyle='--', color='blue', label="Moyenne corrigée")
plt.plot(range(1, len(moyenne_brute)+1), moyenne_brute, marker='o', linestyle='-', color='red', label="Moyenne brute")
plt.xlabel("Semaine de l'année")
plt.ylabel("Consommation")
plt.title("Consommation moyenne brute vs corrigée")
plt.grid(True)
plt.legend()
plt.xticks(range(1, 54, 2))
plt.tight_layout()
plt.show()



#Consommation saisonnière (2018-2024)

import csv
import matplotlib.pyplot as plt

donnees=[]
with open('Evolution_brute_corrigee.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
#        print(','.join(row))
        donnees.append(row)
#print(donnees)


dates_hiver = []
hiver_2024 = []

for element in donnees[1:]:
    date = element[0]
    annee, mois = date.split("-")
    if annee == "2024" and mois in ["12", "01", "02"]:
        dates_hiver.append(date)
        hiver_2024.append(float(element[2].replace(",", ".")))

plt.figure(figsize=(8,4))
plt.plot(dates_hiver, hiver_2024, marker='o', linestyle='-')
plt.title("Consommation hivernale 2024")
plt.xlabel("Date")
plt.ylabel("Valeur")
plt.grid(True)
plt.show()



#Consommation par saison en 2024

import matplotlib.pyplot as plt
#hiver2024
dates_hiver = []
hiver_2024 = []

# On parcourt toutes les données
for mois in ["12", "01", "02"]:  #Par ordre
    for element in donnees[1:]:
        date = element[0]
        annee, m = date.split("-")
        if annee == "2024" and m == mois:
            dates_hiver.append(date)
            hiver_2024.append(float(element[2].replace(",", ".")))

plt.figure(figsize=(8,4))
plt.bar(dates_hiver, hiver_2024, color='skyblue')
plt.title("Consommation hivernale 2024")
plt.xlabel("Mois")
plt.ylabel("Valeur (TWh)")
plt.grid(axis='y') #grille verticale
plt.show()



#Printemps2024
import matplotlib.pyplot as plt

dates_printemps = []
printemps_2024 = []

for mois in ["03", "04", "05"]:  # ordre croissant
    for element in donnees[1:]:
        date = element[0]
        annee, m = date.split("-")
        if annee == "2024" and m == mois:
            dates_printemps.append(date)
            printemps_2024.append(float(element[2].replace(",", ".")))

plt.figure(figsize=(8,4))
plt.bar(dates_printemps, printemps_2024, color='lightgreen')
plt.title("Consommation printemps 2024")
plt.xlabel("Mois")
plt.ylabel("Valeur (TWh)")
plt.grid(axis='y')
plt.show()


#Ete2024
import matplotlib.pyplot as plt

dates_ete = []
ete_2024 = []

for mois in ["06", "07", "08"]: 
    for element in donnees[1:]:
        date = element[0]
        annee, m = date.split("-")
        if annee == "2024" and m == mois:
            dates_ete.append(date)
            ete_2024.append(float(element[2].replace(",", ".")))

plt.figure(figsize=(8,4))
plt.bar(dates_ete, ete_2024, color='orange')
plt.title("Consommation estivale 2024")
plt.xlabel("Mois")
plt.ylabel("Valeur (TWh)")
plt.grid(axis='y')
plt.show()


#Automn2024
import matplotlib.pyplot as plt

dates_automne = []
automne_2024 = []

for mois in ["09", "10", "11"]:
    for element in donnees[1:]:
        date = element[0]
        annee, m = date.split("-")
        if annee == "2024" and m == mois:
            dates_automne.append(date)
            automne_2024.append(float(element[2].replace(",", ".")))

plt.figure(figsize=(8,4))
plt.bar(dates_automne, automne_2024, color='brown')
plt.title("Consommation automne 2024")
plt.xlabel("Mois")
plt.ylabel("Valeur (TWh)")
plt.grid(axis='y')
plt.show()


#Consommation en hiver, printemps, été, automne sur plusieurs années (2018-2020-2022-2024)

import matplotlib.pyplot as plt
import numpy as np

saison = ["12", "01", "02"]  # mois d'hiver
annees = ["2018", "2020", "2022", "2024"]
couleurs = ['skyblue', 'orange', 'lightgreen', 'pink']

#valeurs brutes et corrigées pour chaque année
valeurs_par_annee = []
for annee in annees:
    valeurs = []
    for mois in saison:
        somme_mois = 0
        count = 0
        for element in donnees[1:]:
            date = element[0]
            a, m = date.split("-")
            if a == annee and m == mois:
                somme_mois += float(element[2].replace(",", "."))
                count += 1
        #la moyenne valeurs brutes et corrigées par mois
        if count > 0:
            valeurs.append(somme_mois / count)
        else:
            valeurs.append(0)
    valeurs_par_annee.append(valeurs)

#barres par groupe
x = np.arange(len(saison))  # positions des mois
largeur = 0.2
plt.figure(figsize=(10,5))
for i, valeurs in enumerate(valeurs_par_annee):
    plt.bar(x + i*largeur, valeurs, width=largeur, color=couleurs[i], label=annees[i])
plt.xticks(x + largeur*1.5, ["Déc", "Jan", "Fév"])
plt.title("Consommation hivernale (moyenne des valeurs brutes et corrigées par mois) pour 2018-2020-2022-2024")
plt.xlabel("Mois")
plt.ylabel("Valeur moyenne (TWh)")
plt.legend()
plt.grid(axis='y')
plt.show()


#Printemps
import matplotlib.pyplot as plt
import numpy as np

saison = ["03", "04", "05"]  # mois de printemps
annees = ["2018", "2020", "2022", "2024"]
couleurs = ['skyblue', 'orange', 'lightgreen', 'pink']

#valeurs brutes et corrigées pour chaque année
valeurs_par_annee = []
for annee in annees:
    valeurs = []
    for mois in saison:
        somme_mois = 0
        count = 0
        for element in donnees[1:]:
            date = element[0]
            a, m = date.split("-")
            if a == annee and m == mois:
                somme_mois += float(element[2].replace(",", "."))
                count += 1
        # Moyenne brutes et corrigées par mois
        if count > 0:
            valeurs.append(somme_mois / count)
        else:
            valeurs.append(0)
    valeurs_par_annee.append(valeurs)

#barres par groupe
x = np.arange(len(saison))  # positions des mois
largeur = 0.2
plt.figure(figsize=(10,5))
for i, valeurs in enumerate(valeurs_par_annee):
    plt.bar(x + i*largeur, valeurs, width=largeur, color=couleurs[i], label=annees[i])
plt.xticks(x + largeur*1.5, ["Mars", "Avril", "Mai"])
plt.title("Consommation printanière (moyenne des valeurs brutes et corrigées par mois) 2018-2020-2022-2024")
plt.xlabel("Mois")
plt.ylabel("Valeur moyenne (TWh)")
plt.legend()
plt.grid(axis='y')
plt.show()


#Été
import matplotlib.pyplot as plt
import numpy as np

saison = ["06", "07", "08"]  # mois d'été
annees = ["2018", "2020", "2022", "2024"]
couleurs = ['skyblue', 'orange', 'lightgreen', 'pink']

#valeurs brutes et corrigées pour chaque année
valeurs_par_annee = []
for annee in annees:
    valeurs = []
    for mois in saison:
        somme_mois = 0
        count = 0
        for element in donnees[1:]:
            date = element[0]
            a, m = date.split("-")
            if a == annee and m == mois:
                somme_mois += float(element[2].replace(",", "."))
                count += 1
        # Moyenne des valeurs brutes et corrigées par mois
        if count > 0:
            valeurs.append(somme_mois / count)
        else:
            valeurs.append(0)
    valeurs_par_annee.append(valeurs)


x = np.arange(len(saison))  # positions des mois
largeur = 0.2
plt.figure(figsize=(10,5))
for i, valeurs in enumerate(valeurs_par_annee):
    plt.bar(x + i*largeur, valeurs, width=largeur, color=couleurs[i], label=annees[i])
plt.xticks(x + largeur*1.5, ["Juin", "Juillet", "Août"])
plt.title("Consommation estivale (moyenne des valeurs brutes et corrigées par mois) 2018-2020-2022-2024")
plt.xlabel("Mois")
plt.ylabel("Valeur moyenne (TWh)")
plt.legend()
plt.grid(axis='y')
plt.show()


# Automne
import matplotlib.pyplot as plt
import numpy as np

saison = ["09", "10", "11"]  # mois d'automne
annees = ["2018", "2020", "2022", "2024"]
couleurs = ['skyblue', 'orange', 'lightgreen', 'pink']

#les conso brutes et corrigées pour chaque année
valeurs_par_annee = []

for annee in annees:
    valeurs = []
    for mois in saison:
        somme_mois = 0
        count = 0
        for element in donnees[1:]:
            date = element[0]
            a, m = date.split("-") #sépare la date
            if a == annee and m == mois:
                somme_mois += float(element[2].replace(",", "."))
                count += 1
        # Moyenne brute et corrigée par mois
        if count > 0:
            valeurs.append(somme_mois / count)
        else:
            valeurs.append(0)
    valeurs_par_annee.append(valeurs)

# Tracer barres groupées
x = np.arange(len(saison))  #positions des mois
largeur = 0.2

plt.figure(figsize=(10,5))
for i, valeurs in enumerate(valeurs_par_annee):
    plt.bar(x + i*largeur, valeurs, width=largeur, color=couleurs[i], label=annees[i])

plt.xticks(x + largeur*1.5, ["Septembre", "Octobre", "Novembre"])
plt.title("Consommation automnale (moyenne des valeurs brutes et corrigées par mois) 2018-2020-2022-2024")
plt.xlabel("Mois")
plt.ylabel("Valeur moyenne (TWh)")
plt.legend()
plt.grid(axis='y')
plt.show()


#Consommation moyenne (brute et corrigée) annuelle de 1995 à 2025

import matplotlib.pyplot as plt

#Années de 1995 à 2025
annees = [str(a) for a in range(1995, 2026)]#convertit en str
consommation = []

for annee in annees:
    total = 0
    count = 0
    for element in donnees[1:]:
        date = element[0]
        a, m = date.split("-")
        if a == annee:
            total += float(element[2].replace(",", "."))
            count += 1
    if count > 0:
        consommation.append(total / count)  #moyenne valeurs brutes et corrigées par année
    else:
        consommation.append(0)

# Histogramme
plt.figure(figsize=(12,5))
plt.bar(annees, consommation, color='skyblue')
plt.xticks(rotation=45)
plt.title("Consommation annuelle 1995-2025 (moyenne des valeurs brutes et corrigées)")
plt.xlabel("Année")
plt.ylabel("Valeur moyenne (TWh)")
plt.grid(axis='y')
plt.show()







