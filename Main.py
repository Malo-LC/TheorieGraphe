from importlib.abc import Traversable
import numpy as np
import pandas as pd


df = pd.read_fwf('tableauContrainte2.txt',
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
    # print(indexOmega)
    data = np.insert(data, lin + 1, indexOmega, 0)

    return data


def afficherGraphOrdo(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    print('il y a ', nbSommets(data), ' sommets')
    print('il y a ', nbArcs(data), ' arcs')
    for i in range(1, lin):
        for j in range(0, col):
            if(data[i][j] >= 0 and j >= 2):
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
    print(adjacence)


def getTemps(data, etape):
    return data[etape][1]


tabContr = AlphaOmega(tabContr)
# print(tabContr)
afficherGraphOrdo(tabContr)
matriceAdjacence(tabContr)
