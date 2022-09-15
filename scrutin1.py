import csv
def scrutin1():
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile)
        tab = list(tableau)
        
        indexe = []                                                                   #crée liste vide
        for i, element in enumerate(tab[1]):                                          #parcourir la 1ère ligne
            if element == "1":                                                        #trouver qui est premier
                indexe.append(i)                                                      #ajouter l'indexe du premier dans la liste
        for idx, candidat in enumerate(tab[0]):                                       #parcourir les candidat 
            if idx == indexe[0]:                                                      #faire correspondre les indexes
                print("Le vainqueur est le",candidat, "avec", tab[1][0], "votes.")          

scrutin1()  


        
    

       