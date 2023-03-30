
# Fonctions pour manipuler les rectangles

from configuration.constantes import FORME_CERCLE


def cercle_init(x, y, rayon):
    """
    Fonction pour initialiser un cercle à partir d'une liste de paramètres.

    Arguments:
        x (float): Coordonnée en x du centre du cercle.
        y (float): Coordonnée en y du centre du cercle.
        rayon (float): Rayon du cercle.

    Retourne:
        (dict): Un cercle initialisé.
    """

    return {'x': x, 'y': y, 'rayon': rayon, 'forme': FORME_CERCLE}


def cercle_obtenir_x(cercle):
    """
    Accesseur pour la coordonnée en yx du centre du cercle.

    Arguments:
        cercle (dict): Le cercle.

    Retourne:
        (float): La coordonnée en x du centre du cercle.
    """

    return cercle['x']


def cercle_obtenir_y(cercle):
    """
    Accesseur pour la coordonnée en y du centre du cercle.

    Arguments:
        cercle (dict): Le cercle.

    Retourne:
        (float):  La coordonnée en y du centre du cercle.
    """

    return cercle['y']


def cercle_obtenir_rayon(cercle):
    """
    Accesseur pour le rayon.

    Arguments:
        cercle (dict): Le cercle.

    Retourne:
        (float): Le rayon du cercle.
    """

    return cercle['rayon']


def cercle_afficher(cercle):
    """
    Fonction pour afficher un cercle à la ligne de commande.

    Arguments:
        cercle (dict): Le cercle à afficher.

    Retourne:
        Rien.
    """

    print('Cercle\n',
          f'(xc, yc) : ({cercle_obtenir_x(cercle)},{cercle_obtenir_y(cercle)})\n',
          f'rayon    : {cercle_obtenir_rayon(cercle)}\n')
