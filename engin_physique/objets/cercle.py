
# Fonctions importées
from configuration.constantes import FORME_CERCLE


def cercle_init(x, y, rayon):
    """
    Fonction pour initialiser un cercle à partir d'une liste de paramètres.

    Arguments:
        x (float) : Coordonnée en x du centre du cercle.
        y (float) : Coordonnée en y du centre du cercle.
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


# TODO doit être placé dans engin physique
def cercle_contact_avec_cercle(cercle1, cercle2):
    """
    Cette fonction permet d'identifier si les cercles sont en contact ou non entre eux.

    Arguments:
        cercle1 (dict): cercle 1 à analyser.
        cercle2 (dict) : cercle 2 à analyser.

    Retourne:
        [bool] : indicateur de contact.
    """
    # Extraire les coordonnées des centres des cercles
    x1 = cercle_obtenir_x(cercle1)
    y1 = cercle_obtenir_y(cercle1)
    x2 = cercle_obtenir_x(cercle1)
    y2 = cercle_obtenir_y(cercle1)

    # Extraire les rayons.
    rayon_1 = cercle_obtenir_rayon(cercle1)
    rayon_2 = cercle_obtenir_rayon(cercle2)

    # Calculer la distance entre les centres des cercles.
    distance = pow((x2-x1)**2+(y2-y1)**2, 0.5)

    return distance <= rayon_1 + rayon_2


# TODO faire les deux testes uniformes(p.6)
def test_cercle_en_contact_avec_cercle1():
    pass


def test_cercle_en_contact_avec_cercle2():
    pass
