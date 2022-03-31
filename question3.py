from operator import imod


import numpy as np


def remove_first_match(a, b):
    sidx = b.argsort(kind='mergesort')
    unqb, idx = np.unique(b[sidx], return_index=1)
    return np.delete(b, sidx[idx[np.in1d(unqb, a)]])


def detectionCircuit(adjacence, valeurs):
    print('')
    shape = adjacence.shape
    lin = shape[0]  # On initialise tout
    col = shape[1]
    sommets = adjacence[0]
    sommets = np.delete(sommets, 0)
    PasDePred = np.array([], dtype=int)
    aSupprimer = np.array([], dtype=int)
    # onNote = np.array([], dtype=int)
    cpt = 0
    print('Sommets restants : ', end='')
    print(sommets)
    for i in range(1, col):  # on cherche les sommets sans predecesseurs
        cpt = 0
        for j in range(1, lin):
            # dans le tableau d'adjacence, ceux qui n'ont pas de 1 dans une colonne
            if(adjacence[j][i] == 0):
                cpt += 1
            if(cpt == (lin-1)):
                PasDePred = np.append(PasDePred, adjacence[0][i])
    print('Sommets sans predecesseurs : ', PasDePred)
    print('Suppression des sommets...')
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
        print('')
        print('Il n’y a pas de circuit !')
        return 1
    if(len(PasDePred) == 0 and len(sommets) > 1):
        print('Il y a un circuit !')
        print("Ce n'est pas un graph d'ordonnancement")
        return 0
    return detectionCircuit(adjacence, valeurs)


def detectionOrdonnancement(tabContr):
    shape = tabContr.shape
    lin = shape[0]
    col = shape[1]
    print('Les valeurs pour tous les arcs incidents vers l’extérieur à un sommet sont identiques')
    print('Les arcs ', end='| ')
    for i in range(1, lin):
        for j in range(2, col):
            if(tabContr[i][j] == 0):
                print(tabContr[i][j], '->', i, end=' | ')
    print('sont nuls')
    print("Il n’y a pas d’arcs négatifs")
    print("-> C’est bien un graphe d’ordonnancement")
