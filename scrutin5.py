import csv
def scrutin5():
    listCandidat2 = []
    listCandidat1 = []
    VoteMax = []
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile)
        tab = list(tableau)

    for index in range(len(tab)): 
        for column in range(index+1, len(tab)):                                
        #print(index)
            for Ligne in tab:
            #print(Ligne, "n")
            #print(Ligne[index])
                if index > 1 and column > 1:
                    #break
                #else :
                    #continue
                #print("Element Ligne2 = ", Ligne[index])
                #print("Element Ligne1 = ", Ligne[index-1])
                    if (Ligne[index] > Ligne[index-1]):
                        listCandidat1.append(Ligne[0])
                    else:
                        listCandidat2.append(Ligne[0])
                else :
                    break
            #print("Candidat", index-1 ,"=", listCandidat1)
            #print("Candidat", index,"=", listCandidat2)
            resultat2 = 0
            for chiffre in listCandidat2:
                try:
                    resultat2 += int(chiffre)
                except:
                    pass
            if (resultat2 > 0):
                print(" ")
                #print("candidat", index," = ", resultat, "vs ", end="")
            #VoteMax.append(resultat)
            resultat1 = 0
            for chiffre in listCandidat1:
                try:
                    resultat1 += int(chiffre)
                except:
                    pass
            if (resultat1 > 0):
                print(" ")
                #print("candidat",index-1, " = ", resultat1)
            #VoteMax.append(resultat)
            if resultat1>resultat2 and resultat1 > 1:
                print("candidat",index-1, " gagne son duel contre candidat", index, " avec ", resultat1, " contre ", resultat2)
            else :
                print("candidat",index, " gagne son duel contre candidat", index-1," avec ", resultat2, " contre ", resultat1)
            listCandidat1.clear()
            listCandidat2.clear()
    #print(VoteMax)
    #print(VoteMax[-1])

scrutin5()