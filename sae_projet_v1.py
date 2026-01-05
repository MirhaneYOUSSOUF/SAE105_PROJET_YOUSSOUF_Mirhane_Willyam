import csv
from collections import defaultdict
import matplotlib.pyplot as plt

Donnees=[]
with open('donnees_hebdo.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
#        print(','.join(row))
        Donnees.append(row)
#print(Donnees)

#Donnees semaine 2025

donnees_conso_jour=[]
for element in Donnees:
    if element[0] == 'jour' and element[4] == '2025':
        #print(element[0],element[2], element[6])
        donnees_conso_jour.append(float(element[6].replace(",", ".")))
#print(donnees_conso_jour)

"""
"""
#Donnees de consommation corrigee en semaines

semaine_conso_2025=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2025':
        #print(element[0], element[1], element[2], element[6], element[4])
        #print(element[0:])
        semaine_conso_2025.append(float(element[6].replace(",", ".")))
#print(semaine_conso_2025)

"""



semaine_conso_2024=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2024':
        #print(element[0], element[1], element[2], element[6], element[4])
        semaine_conso_2024.append(float(element[6].replace(",", ".")))
        #print(element[0:])
print(semaine_conso_2024)

"""

semaine_conso_2023=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2023':
        #print(element[0:])
        semaine_conso_2023.append(float(element[6].replace(",", ".")))
#print(semaine_conso_2023)


semaine_conso_2022=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2022':
        #print(element[0:])
        semaine_conso_2022.append(float(element[6].replace(",", ".")))
print(semaine_conso_2022)


semaine_conso_2021=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2021':
        #print(element[0:])
        semaine_conso_2021.append(float(element[6].replace(",", ".")))
#print(semaine_conso_2021)

semaine_conso_2020=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2020':
        #print(element[0:])
        semaine_conso_2020.append(float(element[6].replace(",", ".")))
#print(semaine_conso_2020)















