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
