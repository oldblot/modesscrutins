import csv
def scrutin1():
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile)
        tab = list(tableau)
        #print(tab)
        #classement = sorted(tab[1][1:])
        #print(classement)
        #print(classement[0])
        indexe = []
        #for element in tab:
        #    for idx, case in enumerate(element):
        #        if case == "1":
        #            indexe.append(int(idx)-1)


        for i, element in enumerate(tab[1]):
            if element == "1":
                indexe.append(i)
        for idx, candidat in enumerate(tab[0]):
            if idx == indexe[0]:
                print("Le vainqueur est le",candidat, "avec", tab[1][0], "votes.")

scrutin1()  


        
    

       