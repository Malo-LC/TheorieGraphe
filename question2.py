import numpy as np


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
