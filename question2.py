import numpy as np


def matriceAdjacence(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    s = (lin+1, lin+1)
    adjacence = np.zeros(s, dtype=int)
    # creation de la matrice d'adjacence (que des 0 et le numero de la ligne ou colonne)
    for i in range(1, lin):
        adjacence[0][i+1] = i
        adjacence[i+1][0] = i

    for i in range(0, lin):  # il y a un 1 des qu'il y a une transition entre les 2 etapes
        for j in range(2, col):
            if(data[i][j] >= 0):
                # +1 car il y a la numerotation des lignes et des colonnes
                adjacence[data[i][j]+1][i+1] = 1
    return adjacence


def matriceDesValeurs(data):
    shape = data.shape
    lin = shape[0]
    s = (lin+1, lin+1)
    valeurs = np.zeros(s, dtype='U25')  # matrice de textes
    # initialisation de la matrice
    for i in range(0, lin):
        for j in range(1, lin+1):
            valeurs[i+1][j] = '*'  # etoiles si rien
        valeurs[0][i+1] = i
        valeurs[i+1][0] = i
    # Calcul de la matrice des valeurs

    adjacence = matriceAdjacence(data)
    adjaShape = adjacence.shape
    for i in range(1, adjaShape[0]):
        for j in range(1, adjaShape[1]):
            if(adjacence[i][j] == 1):
                # sinon on met la valeurs de l'etape quand il y' a une transition
                valeurs[i][j] = i-1
    return valeurs
