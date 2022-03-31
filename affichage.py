def nbSommets(data):
    shape = data.shape
    return shape[0]


def getTemps(data, etape):
    return data[etape][1]


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
