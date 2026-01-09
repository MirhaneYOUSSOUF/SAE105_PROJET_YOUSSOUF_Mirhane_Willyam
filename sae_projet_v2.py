import csv

table=[]
with open('_C3_89volution_de_la_consommation_hebdomadaire_2025-12-18_13-41.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        print(','.join(row))
        table.append(row)


for i in range(len(table)):
    if table[i][1]=='2025':
        print(table[i][1],i)
        
table1=[]
with open('_C3_89volution_de_la_consommation_hebdomadaire_2025-12-18_13-41.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        print(','.join(row))
        table.append(row)
A=0
for i in range(len(table1)):
    if table1[i][1]=='2025':
        print(table1[i][1],i)

import csv

table=[]
with open('_C3_89volution_de_la_consommation_hebdomadaire_2025-12-18_13-41.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        print(','.join(row))
        table.append(row)
print(table)
print(table[1][4])


del table[0]
print(table)



for i in range(len(table)):
    table[i][1]=(table[i][1])
print(table)

import csv

fichier_csv = '_C3_89volution_de_la_consommation_hebdomadaire_2025-12-18_13-41.csv'
resultats = []

with open(fichier_csv, newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    header = next(reader)

    for row in reader:
        if row[0] != "semaine":     
            continue
        if row[4] != "2025":        
            continue

        resultats.append({
            "date": row[1],
            "semaine": row[3],
            "conso_corrigee": row[6]
        })

for r in resultats:
    print(r)


#D=[0,0,0,0]
#
#for i in range(len(table)):
#    if table[i][2]<1800:
#        D[0]=D[0]+1
#    elif table[i][2]<1850:
#        D[1]=D[1]+1
#    elif table[i][2]<1900:
#        D[2]=D[2]+1
#    else:
#        D[3]=D[3]+1
#print(D)

import csv
import matplotlib.pyplot as plt

Donnees=[]
with open('_C3_89volution_de_la_consommation_hebdomadaire_2025-12-18_13-41.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        print(','.join(row))
        Donnees.append(row)
print(Donnees)

Donnees1=[]
with open('_C3_89volution_de_la_consommation_hebdomadaire_2025-12-18_13-41.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        print(','.join(row))
        Donnees1.append(row)
print(Donnees1)
print(Donnees1[1][4])


del Donnees1[0]
print(Donnees1)

#Donnees de consommation corrigee en jours pour chaque année (2025, 2024, 2023, 2022, 2021, 2020)

jour_2025=[]
for element in Donnees1:
    if element[0] == 'jour' and element[4] == '2025' and element[6] != 'NA':
        jour_2025.append(float(element[6].replace(',', '.')))  #Convertir en float

for element in Donnees:
    for i in range(6, len(element), 2):
        if element[i] != 'NA' and ligne[i] != '':
            jour_2025.append(float(element[i]))      
print(jour_2025)

jour_2024=[]
for element in Donnees1:
    if element[0] == 'jour' and element[4] == '2024' and element[6] != 'NA':
        jour_2024.append(float(element[6].replace(',', '.')))  #Convertir en float

for element in Donnees:
    for i in range(6, len(element), 2):
        if element[i] != 'NA' and ligne[i] != '':
            jour_2024.append(float(element[i]))      
print(jour_2024)

jour_2023=[]
for element in Donnees1:
    if element[0] == 'jour' and element[4] == '2023' and element[6] != 'NA':
        jour_2023.append(float(element[6].replace(',', '.')))  #Convertir en float

for element in Donnees:
    for i in range(6, len(element), 2):
        if element[i] != 'NA' and ligne[i] != '':
            jour_2023.append(float(element[i]))      
print(jour_2023)

jour_2022=[]
for element in Donnees1:
    if element[0] == 'jour' and element[4] == '2022' and element[6] != 'NA':
        jour_2022.append(float(element[6].replace(',', '.')))  #Convertir en float

for element in Donnees:
    for i in range(6, len(element), 2):
        if element[i] != 'NA' and ligne[i] != '':
            jour_2022.append(float(element[i]))      
print(jour_2022)

jour_2021=[]
for element in Donnees1:
    if element[0] == 'jour' and element[4] == '2021' and element[6] != 'NA':
        jour_2021.append(float(element[6].replace(',', '.')))  #Convertir en float

for element in Donnees:
    for i in range(6, len(element), 2):
        if element[i] != 'NA' and ligne[i] != '':
            jour_2021.append(float(element[i]))      
print(jour_2021)

jour_2020=[]
for element in Donnees1:
    if element[0] == 'jour' and element[4] == '2020' and element[6] != 'NA':
        jour_2020.append(float(element[6].replace(',', '.')))  #Convertir en float

for element in Donnees:
    for i in range(6, len(element), 2):
        if element[i] != 'NA' and ligne[i] != '':
            jour_2020.append(float(element[i]))      
print(jour_2020)

plt.plot(range(1, len(jour_2025)+1), jour_2025, marker='o', label='2025')

plt.plot(range(1, len(jour_2024)+1), jour_2024, marker='o', label='2024')
plt.plot(range(1, len(jour_2023)+1), jour_2023, marker='o', label='2023')
plt.plot(range(1, len(jour_2022)+1), jour_2022, marker='o', label='2022')
plt.plot(range(1, len(jour_2021)+1), jour_2021, marker='o', label="2021")
plt.plot(range(1, len(jour_2020)+1), jour_2020, marker='o', label='2020')

plt.xlabel("Jours de l'année")
plt.ylabel("Consommation corrigée")
plt.title("Évolution hebdomadaire de la consommation (2020 - 2025)")
plt.grid(True)
plt.legend()
plt.show()

import csv
import matplotlib.pyplot as plt

 
Donnees=[]
with open('_C3_89volution_de_la_consommation_hebdomadaire_2025-12-18_13-41.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        #print(','.join(row))
        Donnees.append(row)
#print(Donnees)

entetes = Donnees[0]

idx_maille = entetes.index("maille")
idx_jour_semaine = entetes.index("jour_semaine")

lignes_semaine = [] 



for ligne in Donnees[1:]: 
	maille = ligne[idx_maille] 
	jour_semaine = ligne[idx_jour_semaine] 
	# On garde uniquement les données journalières 
	if maille != 'jour':
		continue 
	if "_" not in jour_semaine:
		continue
	# Récupération du numéro après "_" 
	numero_jour = jour_semaine.split("_")[1] 
	# Jours de semaine : 1 à 5 
	if numero_jour in ["1", "2", "3", "4", "5"]: 
		lignes_semaine.append(ligne) 
#print(lignes_semaine)
		
#Donnees1=[]
#with open('_C3_89volution_de_la_consommation_hebdomadaire_2025-12-18_13-41.csv',newline='') as csvfile:
#    reader=csv.reader(csvfile,delimiter=',')
#    for row in reader:
#        print(','.join(row))
#        Donnees1.append(row)
#print(Donnees1)
#print(Donnees1[1][4])


#del Donnees1[0]
#print(Donnees1)


#semaine5_2025=[]
#for element in semaine5_2025:
#    if element[0] == 'jour' and element[4] == '2025' and element[6] != 'NA':
#        semaine5_2025.append(float(element[6].replace(',', '.')))  #Convertir en float

#for element in lignes_semaine:
#    for i in range(6, len(element), 2):
#        if element[i] != 'NA' and ligne[i] != '':
#            semaine5_2025.append(float(element[i]))      
#print(semaine5_2025)


semaine5_2025=[]
for element in lignes_semaine:
    if element[0] == 'jour' and element[4] == '2025' and element[6] != 'NA':
        semaine5_2025.append(float(element[6].replace(',', '.')))  #Convertir en float
print(semaine5_2025)

plt.plot(range(1, len(semaine5_2025)+1), semaine5_2025, marker='o', label='2025')

#plt.plot(range(1, len(jour_2024)+1), jour_2024, marker='o', label='2024')
#plt.plot(range(1, len(jour_2023)+1), jour_2023, marker='o', label='2023')
#plt.plot(range(1, len(jour_2022)+1), jour_2022, marker='o', label='2022')
#plt.plot(range(1, len(jour_2021)+1), jour_2021, marker='o', label="2021")
#plt.plot(range(1, len(jour_2020)+1), jour_2020, marker='o', label='2020')

plt.xlabel("Lundi-Vendredi de l'année")
plt.ylabel("Consommation corrigée")
plt.title("Évolution hebdomadaire de la consommation de lundi à vendredi (2020 - 2025)")
plt.grid(True)
plt.legend()
plt.show()
