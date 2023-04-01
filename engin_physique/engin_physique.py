
# Fonctions importées
from engin_physique.objets.cercle import cercle_init
from engin_physique.objets.rectangle import rectangle_init

def environnement_init():
    """
    Initialise l'engin physique.

    Arguments:
        nom_fichier (str) : le nom du fichier qui contient l'environnement à charger.

    Retourne:
        (dict): l'environnement initialisé.
    """

    # instantie des objects
    cercle = cercle_init(10, 10, 1)

    # TODO peut-être a enlever?
    rectangle = rectangle_init(20, 20, 10, 5)

    objets = []
    objets.append(cercle)
    objets.append((rectangle))

    return {'objets': objets}


def environnement_obtenir_objets(environnement):
    """
    Accède aux objets de l'environnement.

    Arguments :
        environnement (dict): L'envirionnement.

    Retourne:
        (list): Liste d'objets de l'environnement.
    """

    return environnement['objets']
