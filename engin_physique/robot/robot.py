# Constantes qui définissent le robot
from configuration.constantes import ROBOT_RAYON
from configuration.constantes import ROBOT_X_INITIAL
from configuration.constantes import ROBOT_Y_INITIAL
from configuration.constantes import ROBOT_VITESSE_INITIALE
from configuration.constantes import ROBOT_DIRECTION_INITIALE

# Importer le constructeur de positions
from engin_physique.physique.Position import position_init

# Manipulation des positions (stocker dans un dictionnaire)
from engin_physique.physique.Position import position_obtenir_x
from engin_physique.physique.Position import position_obtenir_y


def robot_init(strategie):
    """
    Fonction pour initialiser à partir du dictionnaire strategie.

    Arguments:
        strategie TODO je sais pas quoi mettre

    Retourne:
        (dict): Une strategie initialiser.
    """

    return {'vitesse': ROBOT_VITESSE_INITIALE,
            'direction': ROBOT_DIRECTION_INITIALE,
            'rayon': ROBOT_RAYON,
            'strategie': strategie,
            'position': position_init(ROBOT_X_INITIAL, ROBOT_Y_INITIAL)}


def robot_obtenir_strategie(robot):
    """
    Accesseur pour la stratégie du robot.

    Arguments:
        robot (dict): Le robot

    Retourne:
        () : la stratégie du robot TODO je sais pas le type
    """

    return robot['strategie']


def robot_obtenir_rayon(robot):
    """
    Accesseur pour le rayon du robot.

    Arguments:
        robot (dict): Le robot

    Retourne:
        (float) : rayon du robot.
    """

    return robot['rayon']


def robot_obtenir_position(robot):
    """
    Accesseur pour la position initial du robot.

    Arguments:
        robot (dict): Le robot

    Retourne:
        (tuple) : coordonnées x et y de la position initiale du robot TODO je sais pas c'est quoi le type
    """
    return robot['position']


def robot_obtenir_vitesse(robot):
    """
    Accesseur pour la vitesse du robot.

    Arguments:
        robot (dict): Le robot

    Retourne:
        (float) : la vitesse du robot.
    """
    return robot['vitesse']


def robot_obtenir_direction(robot):
    """
    Accesseur pour la direction initiale du robot.

    Arguments:
        robot (dict): Le robot

    Retourne:
        (float) : direction initiale du robot.
    """
    return robot['strategie']


def robot_effectuer_deplacement(robot):

    position = robot_obtenir_position(robot)

    # Extraire les composants cartésiens de la position du robot.
    robot_x = position_obtenir_x(position)
    robot_y = position_obtenir_y(position)

    # Extraire ;a direction du robot en radians.
    direction = robot_obtenir_direction(robot)

    # Extraire la vitesse en mètres par iteration.
    vitesse = robot_obtenir_vitesse(robot)

    # Mettre à jour les coordonnées
    robot_x_nouveau = robot_x + cos(direction) * vitesse
    robot_y_nouveau = robot_y + sin(direction) * vitesse
