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


def afficherGraphOrdo(data, f):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    print('il y a ', nbSommets(data), ' sommets')
    f.write('il y a ' + str(nbSommets(data)) + ' sommets\n')
    print('il y a ', nbArcs(data), ' arcs')
    f.write('il y a ' + str(nbArcs(data)) + ' arcs\n')

    for i in range(1, lin):
        for j in range(2, col):
            if(data[i][j] >= 0):
                print(data[i][j], ' -> ', i, ' = ', getTemps(data, data[i][j]))
                f.write(str(data[i][j]) + ' -> ' + str(i) +
                        ' = ' + str(getTemps(data, data[i][j])) + '\n')


def afficherMatValeurs(valeurs, f):
    # affichage de la matrice
    newShape = valeurs.shape
    print('\n ', end='')
    f.write('\n ')
    for i in range(newShape[0]):
        for j in range(newShape[1]):
            if(len(valeurs[i][j]) > 1):
                print(valeurs[i][j], end='  ')
                f.write(str(valeurs[i][j]) + '  ')
            else:
                print(valeurs[i][j], end='   ')
                f.write(str(valeurs[i][j]) + '   ')
        print('')
        f.write('\n')


def afficherRang(data, f):
    f.write('\n\nRang des sommets\n')
    print('\nRang des sommets')
    for i in range(len(data)):
        print(data[i])
        f.write(str(data[i]) + '\n')
