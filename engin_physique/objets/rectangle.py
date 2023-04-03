
# Constantes importées.
from configuration.constantes import FORME_RECTANGLE


def rectangle_init(x, y, largeur, hauteur):
    """
    Fonction pour initialiser un rectangle à partir d'une liste de paramètres.

    Arguments:
        x (float) : coordonnée en x du coin inférieur gauche du rectangle.
        y (float) : coordonnée en y du coin inférieur gauche du rectangle.
        largeur (float) : largeur du rectangle.
        hauteur (float) : hauteur du rectangle.

    Retourne:
        (dict): un rectangle initialisé.
    """

    # Retourner un rectangle initialisé.
    return {'x': x, 'y': y, 'largeur': largeur, 'hauteur': hauteur, 'forme': FORME_RECTANGLE}


def rectangle_obtenir_x1(rectangle):
    """
    Accesseur pour la coordonnée en x du coin inférieur gauche du rectangle.

    Arguments:
        rectangle (dict): le rectangle.

    Retourne:
        (float): la coordonnée en x du coin inférieur gauche du rectangle.
    """

    return rectangle['x']


def rectangle_obtenir_y1(rectangle):
    """
    Accesseur pour la coordonnée en y du coin inférieur gauche sur rectangle.

    Arguments:
        rectangle (dict) : le rectangle.

    Retourne:
        (float): la coordonnée en y du coin inférieur gauche du rectangle.
    """

    return rectangle['y']


def rectangle_obtenir_x2(rectangle):
    """
    Accesseur pour la coordonnée en x du coin supérieur droit du rectangle.

    Arguments:
        rectangle (dict): le rectangle.

    Retourne:
        (float): la coordonnée x du coin supérieur droit du rectangle.
    """

    return rectangle['x'] + rectangle['hauteur']


def rectangle_obtenir_y2(rectangle):
    """
    Accesseur pour la coordonnée y du coin supérieur droit du rectangle.

    Arguments:
        rectangle (dict): le rectangle.

    Retourne:
        (float): la coordonnée y du coin supérieur droit du rectangle.
    """

    return rectangle['y'] + rectangle['largeur']
