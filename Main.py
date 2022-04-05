from asyncore import write
import numpy as np
import initTable
import affichage
import question2
import question3
import question4
import question5
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # Si windows, c'est cls
        command = 'cls'
    os.system(command)


def affichageQuestion():
    print('\n')
    print("Que voulez vous faire ensuite?")
    print("1 - Afficher le graphe d’ordonnancement")
    print("2 - Afficher la matrice d'adjacence et la matrice des valeurs")
    print("3 - Détecter si c'est un graphe d'ordonnancement")
    print("4 - Calculer les rangs de tous les sommets du graphe")
    print("5 - Calculer le calendrier au plus tôt, le calendrier au plus tard et les marges")
    print("6 - Executer toutes les opérations")
    print("7 - Quitter")


def menu():
    clearConsole()
    print('Projet de théorie des graphes.')
    while True:
        try:
            choix = input(
                'Quel table voulez vous choisir ? (entre 1 et 12 inclus)  : ')
            int(choix)
            if(int(choix) < 1 or int(choix) > 12):
                int('pass')
            break
        except ValueError:
            print("Il faut un nombre entre 1 et 12 !!!!")
            pass

    print("Table " + choix + " choisie")
    fichierTrace = open(("TraceTable " + str(choix) + ".txt"), "w")
    tabContr = initTable.choisirTXT(choix)
    tabContr = initTable.AlphaOmega(tabContr)
    matriceAdj = question2.matriceAdjacence(tabContr)
    matriceValeurs = question2.matriceDesValeurs(tabContr)

    affichageQuestion()
    choixSecond = input(
        "Choisissez le nombre correspondant à la ligne : ")
    while (choixSecond != '7'):

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
                df = question5.calendrierTot(tabContr, RangSommet)
                fichierTrace.write('\n')
                fichierTrace.write(df.to_string())
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
                    matriceAdj, matriceValeurs, 0, np.array([]))
                affichage.afficherRang(RangSommet, fichierTrace)
                df = question5.calendrierTot(tabContr, RangSommet)
                fichierTrace.write('\n')
                fichierTrace.write(df.to_string())
            else:
                print('Circuit détecté, impossible de calculer le rang !')
                fichierTrace.write(
                    'Circuit detecte, impossible de calculer le rang !')

        else:
            print('Choix invalide ! ')

        affichageQuestion()
        choixSecond = input(
            "Choisissez le nombre correspondant à la ligne : ")

    return


menu()
