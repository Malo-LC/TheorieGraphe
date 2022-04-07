import numpy as np


def rangDesSommets(adjacence, valeurs, cptRang, RangDuSommet):
    # assez similaire a l'exo 3
    shape = adjacence.shape
    lin = shape[0]  # On initialise tout
    col = shape[1]
    sommets = adjacence[0]
    sommets = np.delete(sommets, 0)
    PasDePred = np.array([], dtype=int)
    aSupprimer = np.array([], dtype=int)
    for i in range(1, col):  # on cherche les sommets sans predecesseurs
        cpt = 0
        for j in range(1, lin):
            # dans le tableau d'adjacence, ceux qui n'ont pas de 1 dans une colonne
            if(adjacence[j][i] == 0):
                cpt += 1
            if(cpt == (lin-1)):
                PasDePred = np.append(PasDePred, adjacence[0][i])

    aAjouterBis = ""
    for i in range(len(PasDePred)):
        aAjouterBis = aAjouterBis + str(PasDePred[i]) + " "
    aAjouter = 'rang ' + str(cptRang) + ' -> ' + aAjouterBis
    while(len(PasDePred) < 5):
        PasDePred = np.append(PasDePred, -1)
    RangDuSommet = np.insert(RangDuSommet, cptRang, PasDePred, axis=0)
    for i in range(len(PasDePred)):  # On supprime les colonnes
        for j in range(1, col):
            if(adjacence[0][j] == PasDePred[i]):
                aSupprimer = np.append(aSupprimer, j)
    adjacence = np.delete(adjacence, aSupprimer, 1)
    valeurs = np.delete(valeurs, aSupprimer, 1)
    shape = adjacence.shape
    lin = shape[0]
    col = shape[1]
    for i in range(1, lin):  # On supprime les valeurs dans les 2 tableaux
        for j in range(1, col):
            if(adjacence[i][j] == 1):
                for k in range(len(PasDePred)):
                    if(int(valeurs[i][j]) == PasDePred[k]):
                        adjacence[i][j] = 0
                        valeurs[i][j] = '*'
                        break
    # On relance la fonction avec les nouveaux tableaux
    if(len(sommets) == 1 and len(PasDePred) != 0):
        return RangDuSommet
    return rangDesSommets(adjacence, valeurs, cptRang+1, RangDuSommet)
