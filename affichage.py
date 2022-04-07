def nbSommets(data):  # nombre de sommets = nb de lignes
    shape = data.shape
    return shape[0]


def getTemps(data, etape):  # temps est sur la 2e colonne de la table des contraintes
    return data[etape][1]


def nbArcs(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    somme = 0

    for i in range(3, col+1):
        for j in range(0, lin):
            # Chaque nombre qui n'est pas dans les 2premieres colonnes est un arc
            if(data[:, i-1:i][j] >= 0):
                somme += 1
    return somme


def afficherGraphOrdo(data, f):
    shape = data.shape
    lin = shape[0]
    col = shape[1]  # affichage
    print('il y a ', nbSommets(data), ' sommets')
    f.write('il y a ' + str(nbSommets(data)) + ' sommets\n')
    print('il y a ', nbArcs(data), ' arcs')
    f.write('il y a ' + str(nbArcs(data)) + ' arcs\n')

    for i in range(1, lin):  # pour toute les etapes dans le tableau
        for j in range(2, col):  # pour le nombre de colonnes
            if(data[i][j] >= 0):  # on fait etape vers une etape et la longueur associée
                print(data[i][j], ' -> ', i, ' = ', getTemps(data, data[i][j]))
                f.write(str(data[i][j]) + ' -> ' + str(i) +
                        ' = ' + str(getTemps(data, data[i][j])) + '\n')


def afficherMatValeurs(valeurs, f):
    # affichage de la matrice
    newShape = valeurs.shape
    print('\n ', end='')
    f.write('\n ')
    # comme la matrice des valeurs est en texte, il faut afficher un par un chaque caractere de la mtrice
    for i in range(newShape[0]):
        for j in range(newShape[1]):
            if(len(valeurs[i][j]) > 1):  # espace plus petit quand c'est un nombre a 2 chiffres
                print(valeurs[i][j], end='  ')
                f.write(str(valeurs[i][j]) + '  ')
            else:
                print(valeurs[i][j], end='   ')
                f.write(str(valeurs[i][j]) + '   ')
        print('')
        f.write('\n')


def afficherRang(data, f):
    f.write('\n\nRang des sommets\n')
    print('\nRang des sommets')  # affichage du rang
    for i in range(len(data)):
        print("Rang ", i, end=" ")
        f.write("Rang ")
        f.write(str(i))
        print("-> ", end="")
        f.write(" -> ")
        for j in range(5):
            if(data[i][j] >= 0):
                # quand il n'y a rien dans la matrice (None normallement) c'est un nombre négatif a la place, donc on affiche que les nombres positifs
                print(data[i][j], end=" ")
                f.write(str(data[i][j]) + ' ')
        print("")
        f.write("\n")
