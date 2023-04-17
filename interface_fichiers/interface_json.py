# from engin_physique.engine_physique import environnement_init
from configuration.constantes import FORME_CERCLE
from configuration.constantes import FORME_RECTANGLE
from configuration.constantes import NOM_FICHIER_INTERFACE_FICHIERS
from configuration.constantes import NOM_FICHIER_EXEMPLES


def creation_fichier():
    """
    Génération d'un fichier d'environnement.

    Arguments:
        Aucun.

    Retourne:
        Rien.
    """

    # Initialiser un environnement.
    environnement = {}

    environnement['objets'] = json_charger_environnement('../interface_fichiers/exemples/piece_complexe.json')
    # Ouvrir le fichier.
    with open(f"..\{NOM_FICHIER_INTERFACE_FICHIERS}\{NOM_FICHIER_EXEMPLES}\obstacles.json", 'w') as fichier:

        # Parcourir les lignes du dictionnaire de chaque objet.
        for ligne in environnement['objets']:

            # Si la clé est de type cercle :
            if ligne['forme'] == FORME_CERCLE:

                # Déterminer les paramètres du cercle.
                x = ligne['x']
                y = ligne['y']
                rayon = ligne['rayon']
                forme = ligne['forme']

                # Ajouter la chaine de caractère au fichier.
                fichier.write("{")
                fichier.write(f'\'x\': {x}, \'y\': {y}, \'rayon\': {rayon}, \'forme\': {forme}')
                fichier.write("}\n")

            # Si la clé est de type rectangle :
            elif ligne['forme'] == FORME_RECTANGLE:

                # Déterminer les paramètres du rectangle.
                x = ligne['x']
                y = ligne['y']
                largeur = ligne['largeur']
                hauteur = ligne['hauteur']
                forme = ligne['forme']

                # Ajouter la chaine de caractère au fichier.
                fichier.write("{")
                fichier.write(f'\'x\': {x}, \'y\': {y}, \'largeur\': {largeur}, \'hauteur\': {hauteur}, \'forme\': '
                              f'{forme}')
                fichier.write("}\n")


def json_charger_environnement(fichier):
    """
    Permet d'intégrer la fonctionnalité du chargement de fichier à votre programme.

    Arguments :
        fichier (class): référence à la classe.

    Retourne :
        liste_obstacles [list] : référence robot vue (inutilisé, mais requis par le module animation).
    """
    with open(fichier, 'r') as environnement:
        texte = environnement.readlines()

    # Initialiser une liste.
    liste_obstacles = []

    for ligne in texte:

        # Caractère à enlever.
        a_enlever = '{}\n'

        # Parcourir la liste.
        for char in a_enlever:
            ligne = ligne.replace(char, '')

        # Spliter la ligne.
        ligne = ligne.split(',')

        # Modifier la liste afin d'obtenir les valeurs du fichier sélectionné.
        dict = {}
        for sous_element in ligne:
            sous_sous_element = sous_element.replace('\'', '').replace(' ', '').split(':')
            # Si le paramètre est une string :
            if sous_sous_element[0] == 'forme':
                dict[sous_sous_element[0]] = sous_sous_element[1]
            # Si le paramètre est un nombre :
            else:
                dict[sous_sous_element[0]] = float(sous_sous_element[1])
        liste_obstacles.append(dict)

    # Retourner la liste d'obstacles.
    return liste_obstacles
