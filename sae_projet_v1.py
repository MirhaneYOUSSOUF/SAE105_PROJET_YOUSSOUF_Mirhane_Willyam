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
        donnees_conso_jour.append(element[6])
#print(donnees_conso_jour)

"""
"""

semaine_2025=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2025':
        #print(element[0], element[1], element[2], element[6], element[4])
        #print(element[0:])
        semaine_2025.append(element[6])
#print(semaine_2025)

"""



semaine_2024=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2024':
        #print(element[0], element[1], element[2], element[6], element[4])
        semaine_2024.append(element[6])
        #print(element[0:])
print(semaine_2024)

"""

semaine_2023=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2023':
        #print(element[0:])
        semaine_2023.append(element[6])
#print(semaine_2023)


semaine_2022=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2022':
        #print(element[0:])
        semaine_2022.append(element[6])
print(semaine_2022)


semaine_2021=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2021':
        #print(element[0:])
        semaine_2021.append(element[6])
#print(semaine_2021)

semaine_2020=[]
for element in Donnees:
    if element[0] == 'semaine' and element[4] == '2020':
        #print(element[0:])
        semaine_2020.append(element[6])
#print(semaine_2020)















