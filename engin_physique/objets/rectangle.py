
# Fonctions importées
from configuration.constantes import FORME_RECTANGLE

# TODO réviser les en-tête et les commentaires

def rectangle_init(x, y, largeur, hauteur, ):
    """
    Fonction pour initialiser un cercle à partir d'une liste de paramètres.

    Arguments:
        x (float) : coordonnée en x du centre du cercle.
        y (float) : coordonnée en y du centre du cercle.
        rayon (float): rayon du cercle.

    Retourne:
        (dict): un cercle initialisé.
    """

    # Retourner un cercle initialé.
    return {'x': x, 'y': y, 'largeur': largeur, 'hauteur': hauteur, 'forme': FORME_RECTANGLE}

# TODO vérifier si le xy dans en-tête est bon dans toutes les fonctions?

def rectangle_obtenir_x1(rectangle):
    """
    Accesseur pour la coordonnée en yx du centre du cercle.

    Arguments:
        rectangle (dict): le cercle.

    Retourne:
        (float): la coordonnée en x du centre du cercle.
    """

    return rectangle['x']


def rectangle_obtenir_y1(rectangle):
    """
    Accesseur pour la coordonnée en yx du centre du cercle.

    Arguments:
        rectangle (dict): le cercle.

    Retourne:
        (float): la coordonnée en x du centre du cercle.
    """

    return rectangle['y']


def rectangle_obtenir_x2(rectangle):
    """
    Accesseur pour la coordonnée en yx du centre du cercle.

    Arguments:
        rectangle (dict): le cercle.

    Retourne:
        (float): la coordonnée en x du centre du cercle.
    """

    return rectangle['x'] + rectangle['hauteur']


def rectangle_obtenir_y2(rectangle):
    """
    Accesseur pour la coordonnée en yx du centre du cercle.

    Arguments:
        rectangle (dict): le cercle.

    Retourne:
        (float): la coordonnée en x du centre du cercle.
    """

    return rectangle['y'] + rectangle['largeur']
