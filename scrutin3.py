import csv 
def scrutin3():
    candidat5 = []
    candidat4 = []
    candidat3 = []
    candidat2 = []
    candidat1 = []
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile)
        tab = list(tableau)                              
        #print(index)
        for Ligne in tab:
            #print(Ligne[3])
            #print(Ligne[index])
            if Ligne[5] == "1":
                candidat5.append(int(Ligne[0]))
            else:
                pass
            if Ligne[4] == "1":
                candidat4.append(int(Ligne[0]))
            else:
                pass
            if Ligne[3] == "1":
                candidat3.append(int(Ligne[0]))
            else:
                pass
            if Ligne[2] == "1":
                candidat2.append(int(Ligne[0]))
            else:
                pass
            if Ligne[1] == "1":
                candidat1.append(int(Ligne[0]))
            else:
                pass
        resultat1 = 0
        for chiffre in candidat5:
            try:
                resultat1 += int(chiffre)
            except:
                pass
        print(resultat1)
        resultat2 = 0
        for chiffre in candidat4:
            try:
                resultat2 += int(chiffre)
            except:
                pass
        print(resultat2)
        resultat3 = 0
        for chiffre in candidat3:
            try:
                resultat3 += int(chiffre)
            except:
                pass
        print(resultat3)
        resultat4 = 0
        for chiffre in candidat2:
            try:
                resultat4 += int(chiffre)
            except:
                pass
        print(resultat4)
        resultat5 = 0
        for chiffre in candidat1:
            try:
                resultat5 += int(chiffre)
            except:
                pass
        print(resultat5)
        


scrutin3()