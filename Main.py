import numpy as np
import pandas as pd


df = pd.read_fwf('table 12.txt',
                 delim_whitespace=True, header=None, engine='python')
# print(df)
tabContr = df.to_numpy(dtype=np.int32)
tabContr[tabContr < 0] = -1


def nbSommets(data):
    shape = data.shape
    return shape[0]


def nbArcs(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    somme = 0

    for i in range(3, col+1):
        for j in range(0, lin):
            if(data[:, i-1:i][j] >= 0):
                somme += 1
    return somme


def ToutLesArcs(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    a = np.array([], dtype=int)

    for i in range(3, col+1):
        for j in range(0, lin):
            if(data[:, i-1:i][j] >= 0):
                a = np.append(a, data[:, i-1:i][j])
    return a


def AlphaOmega(data):
    shape = data.shape
    indexAlpha = np.array([0, 0], dtype=int)
    lin = shape[0]
    col = shape[1]
    arcs = ToutLesArcs(data)
    for i in range(0, col+1):
        if(data[:, 2:3][i] < 0):
            data[:, 2:3][i] = 0
    while(len(indexAlpha) < col):
        indexAlpha = np.append(indexAlpha, -1)

    data = np.insert(data, 0, indexAlpha, 0)

    indexOmega = np.array([[lin + 1, 0]], dtype=int)
    for i in range(1, lin + 1):
        if i in arcs:
            a = 1
        else:
            indexOmega = np.append(indexOmega, i)

    while(len(indexOmega) < col):
        indexOmega = np.append(indexOmega, -1)

    if(len(indexOmega) > col):
        moins1 = np.full(shape=lin+1, fill_value=-1, dtype=np.int32)
        data = np.insert(data, col, moins1, axis=1)
    data = np.insert(data, lin + 1, indexOmega, 0)

    return data


def afficherGraphOrdo(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    print('il y a ', nbSommets(data), ' sommets')
    print('il y a ', nbArcs(data), ' arcs')
    for i in range(1, lin):
        for j in range(2, col):
            if(data[i][j] >= 0):
                print(data[i][j], ' -> ', i, ' = ', getTemps(data, data[i][j]))


def matriceAdjacence(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    s = (lin+1, lin+1)
    adjacence = np.zeros(s, dtype=int)
    for i in range(1, lin):
        adjacence[0][i+1] = i
        adjacence[i+1][0] = i

    for i in range(0, lin):
        for j in range(2, col):
            if(data[i][j] >= 0):
                adjacence[data[i][j]+1][i+1] = 1
    return adjacence


def getTemps(data, etape):
    return data[etape][1]


def matriceDesValeurs(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    s = (lin+1, lin+1)
    valeurs = np.zeros(s, dtype='U25')
    # initialisation de la matrice
    for i in range(0, lin):
        for j in range(1, lin+1):
            valeurs[i+1][j] = '*'
        valeurs[0][i+1] = i
        valeurs[i+1][0] = i
    # Calcul de la matrice des valeurs

    adjacence = matriceAdjacence(data)
    adjaShape = adjacence.shape
    for i in range(1, adjaShape[0]):
        for j in range(1, adjaShape[1]):
            if(adjacence[i][j] == 1):
                valeurs[i][j] = i-1
    return valeurs


def afficherMatValeurs(valeurs):
    # affichage de la matrice
    newShape = valeurs.shape
    print(' ', end='')
    for i in range(newShape[0]):
        for j in range(newShape[1]):
            if(len(valeurs[i][j]) > 1):
                print(valeurs[i][j], end='  ')
            else:
                print(valeurs[i][j], end='   ')
        print('')


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
    for i in range(1, col):
        cpt = 0
        for j in range(1, lin):
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
        detectionOrdonnancement()
        return 1
    if(len(PasDePred) == 0 and len(sommets) > 1):
        print('Il y a un circuit !')
        print("Ce n'est pas un graph d'ordonnancement")
        return 0
    detectionCircuit(adjacence, valeurs)


def detectionOrdonnancement():
    global tabContr
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
    print("-> C’est un graphe d’ordonnancement")


tabContr = AlphaOmega(tabContr)
# print(tabContr)
afficherGraphOrdo(tabContr)


matriceAdj = matriceAdjacence(tabContr)
print('')
print('Matrice d', "'", 'adjacence')
print(matriceAdj)


matriceValeurs = matriceDesValeurs(tabContr)
print('')
print('Matrice des valeurs')
afficherMatValeurs(matriceValeurs)

print('')
print('Detection du circuit')
print('Méthode d’élimination des points d’entrée')
detectionCircuit(matriceAdj, matriceValeurs)
