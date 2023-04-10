from sys import exit
from os import listdir

# Les choix des différents menus
from configuration.constantes import MENU_STRATEGIES
from configuration.constantes import MENU_MODES_OPERATIONS
from configuration.constantes import NOM_FICHIER_EXEMPLES
from configuration.constantes import NOM_FICHIER_INTERFACE_FICHIERS


def afficher_choisir_dictionnaire(dictionnaire, invite):
    # Afficher invite
    print(invite)

    #  Afficher les choix provenant du dictionnaire
    for cle in dictionnaire:
        print(f'\t{cle} - {dictionnaire[cle]}')

    # Mesurer le dictionnaire
    option_quitter = len(dictionnaire)

    # Afficher l<option de quitter
    print(f'\t{option_quitter} - Quitter')

    # Saisir un choix valide
    choix = None
    while choix not in range(option_quitter + 1):
        choix = int(input('Votre choix: '))
        print('\n')

    # Quitter à la demande de l'utilisateur
    if choix == option_quitter:
        exit()

    return choix


def choisir_mode_operation():
    afficher_choisir_dictionnaire(MENU_MODES_OPERATIONS, 'Veuillez choisir le mode d\'opération: ')


def choisir_strategie_robot():
    afficher_choisir_dictionnaire(MENU_STRATEGIES, 'Veuillez choisir la stratégie du robot: ')


if __name__ == '__main__':
    # choisir_mode_operation()
    # choisir_strategie_robot()
    liste_fichier = (listdir('..\\interface_fichiers\\exemples'))

    dictionnaire_menu = {i: nom_fichier for i, nom_fichier in enumerate(liste_fichier)}
