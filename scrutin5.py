import csv
from unittest import result
#def scrutin1():
listCandidat1 = []
listCandidat2 = []
with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
    tableau = csv.reader(csvfile)
    tab = list(tableau)
for ligne in range(len(tab)-1):
    for case in tab: 
        #print(case[ligne])
        if ligne>1:
            #print("case2 = ", case[ligne])
            #print("case1 = ", case[ligne-1])
            if (case[ligne] > case[ligne-1]):
                listCandidat2.append(case[0])
            else:
                listCandidat1.append(case[0])
    #print("List1 = ", listCandidat1)
    #print("List2 = ", listCandidat2)
    resultat = 0
    for element in listCandidat1:
        try:
            resultat += int(element)
        except:
            pass
    if (resultat > 0):
        print("resultat1 = ", resultat)
    resultat = 0
    for element in listCandidat2:
        try:
            resultat += int(element)
        except:
            pass
    if (resultat > 0):
        print("resultat 2 = ", resultat)
    listCandidat2.clear()
    listCandidat1.clear()