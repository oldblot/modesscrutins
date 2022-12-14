import csv

def RemoveCandidat(tab, IndexStocked):
    for Ligne in tab:
        try:
            Ligne.pop(IndexStocked)
        except:
            pass
    return (tab)

def scrutin3(tab):
    result = 1000000
    temporaire = 0
    IndexStocked = 0
    for index in range(1, len(tab)-1):
        for Ligne in tab:
            try:
                if (Ligne[index] == "1" or Ligne[index] == 1):
                    temporaire += int(Ligne[0])
                    #print("temporaire = ", temporaire)
            except:
                pass
        if (result > temporaire and temporaire > 0):
            result = temporaire
            IndexStocked = index
        temporaire = 0
    #print(result, IndexStocked)
    return (tab, IndexStocked)

def GetTab():
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile)
        tab = list(tableau)
        for a, Ligne in enumerate(tab):
            for i, case in enumerate(Ligne):
                try:
                    tab[a][i] = int(case)
                except:
                    pass
    return tab

def ModifyTab(tab):
    for a, Ligne in enumerate(tab):
        for i, case in enumerate(Ligne):
            try:
                if (int(case) > 1 and int(case) < 6):
                    for _ in range(1, len(Ligne)):
                        try:
                            if ((case-1) not in Ligne):
                                tab[a][i] = int(tab[a][i]) - 1
                                tab = ModifyTab(tab)
                                break
                        except:
                            pass
            except:
                pass
    return (tab)

def MainLoop():
    tab = GetTab()
    #print(tab)
    while len(tab[0]) > 2:
        tab, IndexStocked = scrutin3(tab)
        tab = RemoveCandidat(tab, IndexStocked)
        tab = ModifyTab(tab)
    print("Le vainqueur est le", tab[0][1], "!")

MainLoop()