from typing import Type
import initTable
import affichage
import question2
import question3
import question4
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
    print("6 - Quitter")


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

    tabContr = initTable.choisirTXT(choix)
    tabContr = initTable.AlphaOmega(tabContr)
    matriceAdj = question2.matriceAdjacence(tabContr)
    matriceValeurs = question2.matriceDesValeurs(tabContr)

    affichageQuestion()
    choixSecond = input(
        "Choisissez le nombre correspondant à la ligne : ")
    while (choixSecond != '6'):

        if (choixSecond == '1'):
            affichage.afficherGraphOrdo(tabContr)
        elif (choixSecond == '2'):
            print('\n')

            print('Matrice d', "'", 'adjacence')
            print(matriceAdj)
            print('\n')
            print('Matrice des valeurs')
            affichage.afficherMatValeurs(matriceValeurs)
        elif (choixSecond == '3'):
            print('\n')

            print('Detection du circuit')
            print('Méthode d’élimination des points d’entrée')
            if(question3.detectionCircuit(matriceAdj, matriceValeurs) == 1):
                question3.detectionOrdonnancement(tabContr)
            question4.rangDesSommets(matriceAdj, matriceValeurs)

        # elif choixSecond == '4' :

        # elif choixSecond == '5' :

        else:
            print('Choix invalide ! ')

        affichageQuestion()
        choixSecond = input(
            "Choisissez le nombre correspondant à la ligne : ")

    return


menu()
