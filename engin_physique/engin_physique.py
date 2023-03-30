
from engin_physique.objets.cercle import cercle_init


def environnement_init():
    """
    Initialise l'engin physique.

    Arguments:
        nom_fichier (str): Le nom du fichier qui contient l'environnement à charger.

    Retourne:
        (dict): L'environnement initialisé.
    """

    # instantie des objects
    cercle = cercle_init(10, 10, 1)

    objets = []
    objets.append(cercle)

    return {'objets': objets}


def environnement_obtenir_objets(environnement):
    """
    Accède aux objets de l'environnement.

    Arguments:
        environnement (dict): L'envirionnement.

    Retourne:
        (list): Liste d'objets de l'environnement.
    """

    return environnement['objets']
