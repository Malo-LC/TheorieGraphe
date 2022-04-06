import numpy as np
import pandas as pd


def getTemps(data, etape):
    return data[etape][1]


def getPredecesseurs(data, etape):
    shape = data.shape
    col = shape[1]
    resp = np.array([], dtype=int)
    for i in range(2, col):
        if(data[etape][i] >= 0):
            resp = np.append(resp, data[etape][i])
    return resp


def getSuccesseurs(data, etape):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    resp = np.array([], dtype=int)
    for i in range(lin):
        for j in range(2, col):
            if(data[i][j] == etape):
                resp = np.append(resp, data[i][0])
    return resp


def calendrierTot(data, Rang):

    lst = ['Rang', 'Tache', 'longueur', 'Predecesseurs', 'Date par predecesseurs',
           'Date au plus tot']

    tableau = pd.DataFrame(columns=lst)  # creation tableau

    for i in range(len(Rang)):
        rangActuel = i
        Taches = Rang[i]  # a chaque rang, on regarde toute les etapes
        Taches = Taches[Taches >= 0]
        for j in range(len(Taches)):
            EtapeActuelle = Taches[j]
            TempsDeLaTache = getTemps(data, EtapeActuelle)
            predecesseurs = getPredecesseurs(data, EtapeActuelle)

            # Recherche des dates par predecesseurs

            tableauDatePred = np.array([0], dtype=int)  # init
            # pour chaque predecesseur de l'etape actuelle
            for k in range(len(predecesseurs)):
                if(k == 0):
                    tableauDatePred = np.array([], dtype=int)
                # on prend la colonne ou la tache est = au predecesseur
                Recherche = tableau[tableau['Tache']
                                    == predecesseurs[k]]
                # on lui selectionne la date par pred + la longueur
                Dates = Recherche['Date par predecesseurs'].iloc[0]
                Longueur = Recherche['longueur'].iloc[0]
                for l in range(len(Recherche)):
                    # on prend le max de la date par predecesseur et on lui ajoute la longueur
                    DatesPredecesseurs = np.amax(Dates) + Longueur
                    tableauDatePred = np.append(
                        tableauDatePred, DatesPredecesseurs)

            DateAuPlusTot = np.amax(tableauDatePred)
            # on ajoute la ligne au tableau
            tableau.loc[len(tableau.index)] = [
                rangActuel, EtapeActuelle, TempsDeLaTache, predecesseurs, tableauDatePred, DateAuPlusTot]
    return tableau


def calendrierTard(data, Rang):
    lst = ['Rang', 'Tache', 'longueur', 'Successeurs', 'Date par Successeurs',
           'Date au plus Tard']

    tableau = pd.DataFrame(columns=lst)
    startindex = len(Rang)-1
    stopindex = -1
    step = -1  # boucle for a l'envers, on commence par la fin
    calTot = calendrierTot(data, Rang)
    tempsCalTot = calTot.iloc[-1]
    tempsCalTot = tempsCalTot['Date au plus tot']
    for i in range(startindex, stopindex, step):
        rangActuel = i
        Taches = Rang[i]
        Taches = Taches[Taches >= 0]
        for j in range(len(Taches)):
            EtapeActuelle = Taches[j]
            TempsDeLaTache = getTemps(data, EtapeActuelle)
            Successeurs = getSuccesseurs(data, EtapeActuelle)
            # Recherche des dates par Successeurs

            tableauDatePred = np.array([tempsCalTot], dtype=int)
            for k in range(len(Successeurs)):
                if(k == 0):
                    tableauDatePred = np.array([], dtype=int)
                Recherche = tableau[tableau['Tache']
                                    == Successeurs[k]]
                # quasiment pareil sauf que l'on prend les successeurs
                Dates = Recherche['Date par Successeurs'].iloc[0]

                for l in range(len(Recherche)):
                    # minimum des dates - la longueur
                    DatesSuccesseurs = np.amin(Dates) - TempsDeLaTache
                    tableauDatePred = np.append(
                        tableauDatePred, DatesSuccesseurs)

            DateAuPlusTard = np.amin(tableauDatePred)
            # on ajoute l'etape
            tableau.loc[-1] = [
                rangActuel, EtapeActuelle, TempsDeLaTache, Successeurs, tableauDatePred, DateAuPlusTard]
            tableau.index = tableau.index + 1
            tableau.sort_index(inplace=True)
    tableau = tableau.sort_values(by=['Rang', 'Tache'])
    return tableau


def calculMarges(calTot, calTard):
    dateAuPlusTot = calTot['Date au plus tot']
    dateAuPlusTard = calTard['Date au plus Tard']
    rang = calTot['Rang']
    Tache = calTot['Tache']
    longueur = calTot['longueur']
    Marges = dateAuPlusTard - dateAuPlusTot
    df = pd.DataFrame()
    df['Rang'] = rang
    df['Tache'] = Tache
    df['Longueur'] = longueur
    df['Date au plus tot'] = dateAuPlusTot
    df['Date au plus tard'] = dateAuPlusTard
    df['Marge totale'] = Marges
    return df
