import numpy as np
import initTable
import affichage
import question2  # Import des fonctions, deuis les autres fichiers
import question3
import question4
import question5
import os


def clearConsole():  # clear la console
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si windows, c'est cls
        command = 'cls'
    os.system(command)


def affichageQuestion():  # afficher les questions
    print('\n')
    print("Que voulez vous faire ensuite?")
    print("1 - Afficher le graphe d’ordonnancement")
    print("2 - Afficher la matrice d'adjacence et la matrice des valeurs")
    print("3 - Détecter si c'est un graphe d'ordonnancement")
    print("4 - Calculer les rangs de tous les sommets du graphe")
    print("5 - Calculer le calendrier au plus tôt, le calendrier au plus tard et les marges")
    print("6 - Executer toutes les opérations")
    print("7 - Quitter")
    print("8 - Executer toutes les opérations sur tout les fichiers")


def ToutPartout():
    for i in range(1, 13):  # boucle pour executer tout dans les 12 fichiers
        choix = str(i)
        print("Table " + choix + " choisie")
        fichierTrace = open(("TraceTable " + str(choix) + ".txt"), "w")
        tabContr = initTable.choisirTXT(choix)
        tabContr = initTable.AlphaOmega(tabContr)
        matriceAdj = question2.matriceAdjacence(tabContr)
        matriceValeurs = question2.matriceDesValeurs(tabContr)
        affichage.afficherGraphOrdo(tabContr, fichierTrace)

        print('\nMatrice d', "'", 'adjacence')
        fichierTrace.write('\n Matrice d' + "'" + 'adjacence\n')
        print(matriceAdj)
        fichierTrace.write(str(matriceAdj))
        print('\nMatrice des valeurs')
        fichierTrace.write('\nMatrice des valeurs\n')
        affichage.afficherMatValeurs(matriceValeurs, fichierTrace)

        print('\nDetection du circuit')
        fichierTrace.write('\nDetection du circuit')
        print('\nMéthode d’élimination des points d’entrée')
        fichierTrace.write("\nMethode d'elimination des points d'entree")
        if(question3.detectionCircuit(matriceAdj, matriceValeurs, fichierTrace) == 1):
            question3.detectionOrdonnancement(tabContr, fichierTrace)
            RangSommet = question4.rangDesSommets(
                matriceAdj, matriceValeurs, 0, np.empty((0, 5), dtype=int))
            affichage.afficherRang(RangSommet, fichierTrace)
            print('')

            print("Dates au plus tôt")
            calTot = question5.calendrierTot(tabContr, RangSommet)
            print(calTot)
            fichierTrace.write('\n')
            fichierTrace.write('Dates au plus tot\n')
            fichierTrace.write(calTot.to_string())
            fichierTrace.write('\n')

            print("")
            print("Dates au plus tard")

            calTard = question5.calendrierTard(tabContr, RangSommet)
            print(calTard)
            fichierTrace.write('\n')
            fichierTrace.write('Dates au plus tard\n')

            fichierTrace.write(calTard.to_string())
            fichierTrace.write('\n')

            marge = question5.calculMarges(calTot, calTard)
            print("")
            print("Marge Totale")
            print(marge)

            fichierTrace.write('\n')
            fichierTrace.write('Marge Totale\n')

            fichierTrace.write(marge.to_string())
            fichierTrace.write('\n')

        else:
            print('Circuit détecté, impossible de calculer le rang !')
            fichierTrace.write(
                'Circuit detecte, impossible de calculer le rang !')


def menu():  # Menu de choix de la question
    clearConsole()
    print('Projet de théorie des graphes.')
    print('Malo Le Corvec - Baptiste Keunebroek - Clement Le Corre - Tony Koudache')
    while True:
        # sécurité pour le choix du fichier (un nombre entre 1 et 12, et pas une lettre)
        try:
            choix = input(
                'Quel table voulez vous choisir ? (entre 1 et 12 inclus)  : ')
            int(choix)
            if(int(choix) < 1 or int(choix) > 12):
                int('pass')
            break
        except ValueError:  # si c'est pas un int
            print("Il faut un nombre entre 1 et 12 !!!!")
            pass

    print("Table " + choix + " choisie")
    fichierTrace = open(("TraceTable " + str(choix) + ".txt"), "w")
    # initialisation des données necessaires pour la suite
    tabContr = initTable.choisirTXT(choix)
    tabContr = initTable.AlphaOmega(tabContr)
    matriceAdj = question2.matriceAdjacence(tabContr)
    matriceValeurs = question2.matriceDesValeurs(tabContr)

    affichageQuestion()
    choixSecond = input(
        "Choisissez le nombre correspondant à la ligne : ")
    while (choixSecond != '7'):  # faire un choix
        # pour chaque choix, on lance la fonction associé et on affiche les résultats
        if (choixSecond == '1'):
            affichage.afficherGraphOrdo(tabContr, fichierTrace)
        elif (choixSecond == '2'):
            print('\nMatrice d', "'", 'adjacence')
            fichierTrace.write('\n Matrice d' + "'" + 'adjacence\n')

            print(matriceAdj)
            fichierTrace.write(str(matriceAdj))

            print('\nMatrice des valeurs')
            fichierTrace.write('\nMatrice des valeurs\n')

            affichage.afficherMatValeurs(matriceValeurs, fichierTrace)
        elif (choixSecond == '3'):
            print('\nDetection du circuit')
            fichierTrace.write('\nDetection du circuit')

            print('\nMéthode d’élimination des points d’entrée')
            fichierTrace.write("\nMethode d'elimination des points d'entree")

            if(question3.detectionCircuit(matriceAdj, matriceValeurs, fichierTrace) == 1):
                question3.detectionOrdonnancement(tabContr, fichierTrace)

        elif choixSecond == '4':

            print('\nDetection du circuit')
            fichierTrace.write('\nDetection du circuit')

            print('\nMéthode d’élimination des points d’entrée')
            fichierTrace.write("\nMethode d'elimination des points d'entree")

            if(question3.detectionCircuit(matriceAdj, matriceValeurs, fichierTrace) == 1):
                question3.detectionOrdonnancement(tabContr, fichierTrace)
                RangSommet = question4.rangDesSommets(
                    matriceAdj, matriceValeurs, 0, np.empty((0, 5), dtype=int))
                affichage.afficherRang(RangSommet, fichierTrace)
            else:
                print('Circuit détecté, impossible de calculer le rang !')
                fichierTrace.write(
                    'Circuit detecte, impossible de calculer le rang !')

        elif choixSecond == '5':

            if(question3.detectionCircuit(matriceAdj, matriceValeurs, fichierTrace) == 1):
                question3.detectionOrdonnancement(tabContr, fichierTrace)
                RangSommet = question4.rangDesSommets(
                    matriceAdj, matriceValeurs, 0, np.empty((0, 5), dtype=int))
                print('')

                print("Dates au plus tôt")
                calTot = question5.calendrierTot(tabContr, RangSommet)
                print(calTot)
                fichierTrace.write('\n')
                fichierTrace.write('Dates au plus tot\n')
                fichierTrace.write(calTot.to_string())
                fichierTrace.write('\n')

                print("")
                print("Dates au plus tard")

                calTard = question5.calendrierTard(tabContr, RangSommet)
                print(calTard)
                fichierTrace.write('\n')
                fichierTrace.write('Dates au plus tard\n')

                fichierTrace.write(calTard.to_string())
                fichierTrace.write('\n')

                marge = question5.calculMarges(calTot, calTard)
                print("")
                print("Marge Totale")
                print(marge)

                fichierTrace.write('\n')
                fichierTrace.write('Marge Totale\n')

                fichierTrace.write(marge.to_string())
                fichierTrace.write('\n')

            else:
                print('Circuit détecté, impossible de calculer le rang !')
                fichierTrace.write(
                    'Circuit detecte, impossible de calculer le rang !')

        elif choixSecond == '6':
            affichage.afficherGraphOrdo(tabContr, fichierTrace)

            print('\nMatrice d', "'", 'adjacence')
            fichierTrace.write('\n Matrice d' + "'" + 'adjacence\n')
            print(matriceAdj)
            fichierTrace.write(str(matriceAdj))
            print('\nMatrice des valeurs')
            fichierTrace.write('\nMatrice des valeurs\n')
            affichage.afficherMatValeurs(matriceValeurs, fichierTrace)

            print('\nDetection du circuit')
            fichierTrace.write('\nDetection du circuit')
            print('\nMéthode d’élimination des points d’entrée')
            fichierTrace.write("\nMethode d'elimination des points d'entree")
            if(question3.detectionCircuit(matriceAdj, matriceValeurs, fichierTrace) == 1):
                question3.detectionOrdonnancement(tabContr, fichierTrace)
                RangSommet = question4.rangDesSommets(
                    matriceAdj, matriceValeurs, 0, np.empty((0, 5), dtype=int))
                affichage.afficherRang(RangSommet, fichierTrace)
                print('')

                print("Dates au plus tôt")
                calTot = question5.calendrierTot(tabContr, RangSommet)
                print(calTot)
                fichierTrace.write('\n')
                fichierTrace.write('Dates au plus tot\n')
                fichierTrace.write(calTot.to_string())
                fichierTrace.write('\n')

                print("")
                print("Dates au plus tard")

                calTard = question5.calendrierTard(tabContr, RangSommet)
                print(calTard)
                fichierTrace.write('\n')
                fichierTrace.write('Dates au plus tard\n')

                fichierTrace.write(calTard.to_string())
                fichierTrace.write('\n')

                marge = question5.calculMarges(calTot, calTard)
                print("")
                print("Marge Totale")
                print(marge)

                fichierTrace.write('\n')
                fichierTrace.write('Marge Totale\n')

                fichierTrace.write(marge.to_string())
                fichierTrace.write('\n')

            else:
                print('Circuit détecté, impossible de calculer le rang !')
                fichierTrace.write(
                    'Circuit detecte, impossible de calculer le rang !')

        elif choixSecond == '8':
            ToutPartout()
        else:
            print('Choix invalide ! ')

        affichageQuestion()
        choixSecond = input(
            "Choisissez le nombre correspondant à la ligne : ")

    return


menu()
