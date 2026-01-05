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













