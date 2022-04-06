import numpy as np
import pandas as pd


def choisirTXT(choix):
    df = pd.read_fwf('table ' + str(choix) + '.txt',
                     delim_whitespace=True, header=None, engine='python')  # choix du fichier
    # print(df)
    tabContr = df.to_numpy(dtype=np.int32)  # transformation en numpy
    tabContr[tabContr < 0] = -1  # on remplace les None par des -1
    return tabContr


def ToutLesArcs(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    a = np.array([], dtype=int)
# creation d'un tableau avec tout les arcs de la matrice
    for i in range(3, col+1):
        for j in range(0, lin):
            if(data[:, i-1:i][j] >= 0):
                a = np.append(a, data[:, i-1:i][j])
    return a


def AlphaOmega(data):
    shape = data.shape
    indexAlpha = np.array([0, 0], dtype=int)
    lin = shape[0]
    col = shape[1]  # rajouter alpha et omega
    arcs = ToutLesArcs(data)
    for i in range(0, col+1):  # ceux qui n'ont pas de predecesseurs auront alpha
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
            # ceux qui n'ont pas de successeurs auront Omega
            indexOmega = np.append(indexOmega, i)

    while(len(indexOmega) < col):
        indexOmega = np.append(indexOmega, -1)

    if(len(indexOmega) > col):  # il faut que la taille des tableaux soit les memes pour etre ajoutés entre eux
        moins1 = np.full(shape=lin+1, fill_value=-1, dtype=np.int32)
        data = np.insert(data, col, moins1, axis=1)
    data = np.insert(data, lin + 1, indexOmega, 0)

    return data
