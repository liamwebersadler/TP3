from sys import exit
from os import listdir

# Les choix des différents menus.
from configuration.constantes import MENU_STRATEGIES
from configuration.constantes import MENU_MODES_OPERATIONS
from engin_physique.engine_physique import environnement_init


def afficher_choisir_dictionnaire(dictionnaire, invite):
    # Afficher invite.
    print(invite)

    #  Afficher les choix provenant du dictionnaire.
    for cle in dictionnaire:
        print(f'\t{cle} - {dictionnaire[cle]}')

    # Mesurer le dictionnaire.
    option_quitter = len(dictionnaire)

    # Afficher l'option de quitter.
    print(f'\t{option_quitter} - Quitter')

    # Saisir un choix valide.
    choix = None
    while choix not in range(option_quitter + 1):
        choix = int(input('Votre choix: '))
        print('\n')

    # Quitter à la demande de l'utilisateur.
    if choix == option_quitter:
        exit()

    return dictionnaire[choix]


def choisir_mode_operation():
    return afficher_choisir_dictionnaire(MENU_MODES_OPERATIONS, 'Veuillez choisir le mode d\'opération: ')


def choisir_strategie_robot():
    return afficher_choisir_dictionnaire(MENU_STRATEGIES, 'Veuillez choisir la stratégie du robot: ')


def choisir_environnement(path):
    # Extraire les noms de fichiers de l'environnement.
    liste_fichier = listdir(path)

    # Construire un dictionnaire pour l'affichage du menu.
    dictionnaire_menu = {i: nom_fichier for i, nom_fichier in enumerate(liste_fichier)}

    # Afficher le menu.
    choix_user = afficher_choisir_dictionnaire(dictionnaire_menu, 'Veuillez choisir l\'environnement')

    return environnement_init(path + '/' + choix_user)
