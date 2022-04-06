import numpy as np


def remove_first_match(a, b):  # fonction pour supprimer des qu'on trouve le meme
    sidx = b.argsort(kind='mergesort')
    unqb, idx = np.unique(b[sidx], return_index=1)
    return np.delete(b, sidx[idx[np.in1d(unqb, a)]])


def detectionCircuit(adjacence, valeurs, f):
    print('\n')
    f.write('\n')
    shape = adjacence.shape
    lin = shape[0]  # On initialise tout
    col = shape[1]
    sommets = adjacence[0]
    sommets = np.delete(sommets, 0)
    PasDePred = np.array([], dtype=int)
    aSupprimer = np.array([], dtype=int)
    cpt = 0
    print('Sommets restants : ', end='')
    f.write('Sommets restants : ')
    print(sommets)
    f.write(str(sommets) + '\n')
    for i in range(1, col):  # on cherche les sommets sans predecesseurs
        cpt = 0
        for j in range(1, lin):
            # dans le tableau d'adjacence, ceux qui n'ont pas de 1 dans une colonne de la matrice d'adjacence
            # ca veut dire qu'il n'a pas de predecesseur
            if(adjacence[j][i] == 0):
                cpt += 1
            if(cpt == (lin-1)):  # si le compteur = au nb de lignes, c'est que la colonne est rempli de 0
                # on le retient dans une liste
                PasDePred = np.append(PasDePred, adjacence[0][i])
    print('Sommets sans predecesseurs : ', PasDePred)
    f.write('Sommets sans predecesseurs : ' + str(PasDePred) + '\n')
    print('Suppression des sommets...')
    f.write('Suppression des sommets...' + '\n')
    for i in range(len(PasDePred)):  # On supprime les colonnes sans predecesseurs
        for j in range(1, col):
            if(adjacence[0][j] == PasDePred[i]):
                aSupprimer = np.append(aSupprimer, j)
    # dans la matrice d'adjacence et des valeurs
    adjacence = np.delete(adjacence, aSupprimer, 1)
    valeurs = np.delete(valeurs, aSupprimer, 1)
    shape = adjacence.shape
    lin = shape[0]
    col = shape[1]
    for i in range(1, lin):  # Puis on supprime les valeurs dans les 2 tableaux
        for j in range(1, col):  # on parcours toute la matrice
            if(adjacence[i][j] == 1):
                for k in range(len(PasDePred)):
                    if(int(valeurs[i][j]) == PasDePred[k]):
                        # si on remarque que la valeurs est celle que l'on vient de supprimer, on la supprime aussi a l'intérieur de a matrice
                        adjacence[i][j] = 0
                        valeurs[i][j] = '*'
                        break
    # conditions de fin
    # si il y a plus qu'un sommet et qu'il n'a pas de predecesseur (logique), c'est fini
    if(len(sommets) == 1 and len(PasDePred) != 0):
        print('\nIl n’y a pas de circuit !')
        f.write("\nIl n'y a pas de circuit !\n")
        return 1
    # si il nous reste des sommets dans le tableau mais que il n'y a pas d'etapes sans predecesseurs, il y a un circuit
    if(len(PasDePred) == 0 and len(sommets) > 1):
        print("Il y a un circuit ! \n Ce n'est pas un graph d'ordonnancement")
        f.write("Il y a un circuit ! \n Ce n'est pas un graph d'ordonnancement")
        return 0
    # On relance la fonction avec les nouveaux tableaux actualisés
    return detectionCircuit(adjacence, valeurs, f)


def detectionOrdonnancement(tabContr, f):
    shape = tabContr.shape
    lin = shape[0]
    col = shape[1]
    # impossible que ca soit different dans le tableau de contrainte
    print('Les valeurs pour tous les arcs incidents vers l’extérieur à un sommet sont identiques')
    f.write("Les valeurs pour tous les arcs incidents vers l'exterieur a un sommet sont identiques\n")
    print('Les arcs ', end='| ')
    f.write('Les arcs | ')
    for i in range(1, lin):
        for j in range(2, col):
            if(tabContr[i][j] == 0):
                # affichage des transitions de alpha
                print(tabContr[i][j], '->', i, end=' | ')
                f.write(str(tabContr[i][j]) + ' -> ' + str(i) + ' | ')
    # pas d'arcs négatifs car ils sont supprimés a l'initialisation du tableau
    print("sont nuls \nIl n'y a pas d’arcs négatifs\n -> C’est bien un graphe d’ordonnancement")
    f.write("sont nuls \nIl n'y a pas d'arcs negatifs\n -> C'est bien un graphe d'ordonnancement")
