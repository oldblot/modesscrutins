import csv
#def scrutin1():
listCandidat2 = []
listCandidat1 = []
with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
    tableau = csv.reader(csvfile)
    tab = list(tableau)
for index in range(len(tab)-1):
    #print(index)
    for Ligne in tab:
        #print(Ligne, "n")
        #print(Ligne[index])
        if index>1:
            #print("Element Ligne2 = ", Ligne[index])
            #print("Element Ligne1 = ", Ligne[index-1])
            if (Ligne[index] > Ligne[index-1]):
                listCandidat1.append(Ligne[0])
            else:
                listCandidat2.append(Ligne[0])
    #print("Candidat", index-1 ,"=", listCandidat1)
    #print("Candidat", index,"=", listCandidat2)
    resultat = 0
    for chiffre in listCandidat2:
        try:
            resultat += int(chiffre)
        except:
            pass
    if (resultat > 0):
        print("candidat", index," = ", resultat, "vs ", end="")
    resultat = 0
    for chiffre in listCandidat1:
        try:
            resultat += int(chiffre)
        except:
            pass
    if (resultat > 0):
        print("candidat",index-1, " = ", resultat)
    listCandidat1.clear()
    listCandidat2.clear()