
# Fonctions pour manipuler les rectangles

from configuration.constantes import FORME_RECTANGLE

# TODO révisiser les en-tête et les commentaires


def rectangle_init(x, y, largeur, hauteur, ):
    """
    Fonction pour initialiser un cercle à partir d'une liste de paramètres.

    Arguments:
        x (float) : Coordonnée en x du centre du cercle.
        y (float) : Coordonnée en y du centre du cercle.
        rayon (float): Rayon du cercle.

    Retourne:
        (dict): Un cercle initialisé.
    """

    return {'x': x, 'y': y, 'largeur': largeur, 'hauteur': hauteur, 'forme': FORME_RECTANGLE}


def rectangle_obtenir_x1(rectangle):
    """
    Accesseur pour la coordonnée en yx du centre du cercle.

    Arguments:
        cercle (dict): Le cercle.

    Retourne:
        (float): La coordonnée en x du centre du cercle.
    """

    return rectangle['x']


def rectangle_obtenir_y1(rectangle):
    """
    Accesseur pour la coordonnée en yx du centre du cercle.

    Arguments:
        cercle (dict): Le cercle.

    Retourne:
        (float): La coordonnée en x du centre du cercle.
    """

    return rectangle['y']


def rectangle_obtenir_x2(rectangle):
    """
    Accesseur pour la coordonnée en yx du centre du cercle.

    Arguments:
        cercle (dict): Le cercle.

    Retourne:
        (float): La coordonnée en x du centre du cercle.
    """

    return rectangle['x'] + rectangle['hauteur']


def rectangle_obtenir_y2(rectangle):
    """
    Accesseur pour la coordonnée en yx du centre du cercle.

    Arguments:
        cercle (dict): Le cercle.

    Retourne:
        (float): La coordonnée en x du centre du cercle.
    """

    return rectangle['y'] + rectangle['largeur']
