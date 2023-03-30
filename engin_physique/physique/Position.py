
def position_init(x, y):
    """
    Fonction d'initialisation d'une position.

    Arguments:
        x (float): La coordonnée en x.
        y (float): La coordonnée en y.

    Retourne:
        (dict): La position initialisée.
    """

    return {'x': x, 'y': y}


def position_afficher(une_position):
    """
    Affiche une position à la ligne de commande.

    Arguments:
        Une position (dict): La position à afficher.

    Retourne:
        Rien.
    """

    print(f'x: {position_obtenir_x(une_position)}',
          f'y: {position_obtenir_y(une_position)}')


def position_obtenir_x(une_position):
    """
    Accède à la coordonnée en x d'une position.

    Arguments:
        une_position (dict): La position à consulter.

    Retourne:
        Rien.
    """

    return une_position['x']


def position_obtenir_y(une_position):
    """
    Accède à la coordonnée en y d'une position.

    Arguments:
        une_position (dict): La position à consulter.

    Retourne:
        Rien.
    """

    return une_position['y']


def position_modifier_x(une_position, nouveau_x):
    """
    Modifie la coordonnée en x d'une position.

    Arguments:
        une_position (dict): La position à modifier.
        nouveau_x (float): La nouvelle position.

    Retourne:
        Rien.
    """

    une_position['x'] = nouveau_x


def position_modifier_y(une_position, nouveau_y):
    """
    Modifie la coordonnée en y d'une position.

    Arguments:
        une_position (dict): La position à modifier.
        nouveau_y (float): La nouvelle position.

    Retourne:
        Rien.
    """

    une_position['y'] = nouveau_y


def position_soustraire(position_1, position_2):
    """
    Calcule le résultat de la soustraction de deux positions.

    Arguments:
        position_1 (dict): La première position.
        position_2 (dict): La deuxième position.

    Retourne:
        (dict): Une nouvelle position qui représente la différence des deux reçues.
    """

    # Extraire les coordonnées de la première position
    x1 = position_obtenir_x(position_1)
    y1 = position_obtenir_y(position_1)

    # Extraire les coordonnées de la deuxième position
    x2 = position_obtenir_x(position_2)
    y2 = position_obtenir_y(position_2)

    return position_init(x2 - x1, y2 - y1)
