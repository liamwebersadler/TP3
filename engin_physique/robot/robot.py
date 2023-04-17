# Constantes qui définissent le robot.
from configuration.constantes import ROBOT_RAYON
from configuration.constantes import ROBOT_X_INITIAL
from configuration.constantes import ROBOT_Y_INITIAL
from configuration.constantes import ROBOT_VITESSE_INITIALE
from configuration.constantes import ROBOT_DIRECTION_INITIALE

# Constantes générales.
from configuration.constantes import DEVIATION_MOUVEMENT_ALEATOIRE

# Importer le constructeur de positions.
from engin_physique.physique.Position import position_init

# Manipulation des positions (stocker dans un dictionnaire).
from engin_physique.physique.Position import position_obtenir_x
from engin_physique.physique.Position import position_obtenir_y

# Fonction mathématique.
from math import sin
from math import cos
from math import pi

# Générateur(s) de nombre aléatoire.
from numpy.random import normal


def robot_init(strategie):
    """
    Fonction pour initialiser à partir du dictionnaire strategie.

    Arguments :
        strategie (dict) : Dictionnaire qui retourne les stratégies du robot.

    Retourne :
        (dict): Une stratégie initialiser.
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
         : la stratégie du robot TODO je sais pas le type
    """

    return robot['strategie']


def robot_obtenir_rayon(robot):
    """
    Accesseur pour le rayon du robot.

    Arguments:
        robot (dict): le robot

    Retourne:
        (float) : rayon du robot.
    """

    return robot['rayon']


def robot_obtenir_position(robot):
    """
    Accesseur pour la position initial du robot.

    Arguments:
        robot (dict): le robot.

    Retourne:
        position du robot (tuple) : coordonnées x et y de la position initiale du robot T.
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
    """
    return robot['direction']


def robot_modifier_position(robot, nouvelle_position):
    """
    Modifie la position du robot.

    Arguments:
        robot (dict): robot
        nouvelle_position (dict): nouvelle position du robot

    Retour :
        Rien.
    """

    robot['position'] = nouvelle_position


def robot_obtenir_prochaine_position(robot):
    """
    Retourne la nouvelle position du robot

    Argument:
        robot {dict}: robot.

    Retour :
        {dict}: nouvelle position du robot.
    """

    position = robot_obtenir_position(robot)

    # Extraire les composants cartésiens de la position du robot.
    robot_x = position_obtenir_x(position)
    robot_y = position_obtenir_y(position)

    # Extraire ;a direction du robot en radians.
    direction = robot_obtenir_direction(robot)

    # Extraire la vitesse en mètres par iteration.
    vitesse = robot_obtenir_vitesse(robot)

    # Mettre à jour les coordonnées.
    robot_x_nouveau = robot_x + cos(direction) * vitesse
    robot_y_nouveau = robot_y + sin(direction) * vitesse

    # Créer la nouvelle position.
    position_nouvelle = position_init(robot_x_nouveau, robot_y_nouveau)

    return position_nouvelle


def robot_effectuer_deplacement(robot):
    """
    Assigne la nouvelle position du robot.

    Arguments :
        robot (dict): robot.

    Retour :
        Rien.
    """

    # Calculer la prochaine position.
    nouvelle_position = robot_obtenir_prochaine_position(robot)

    # Assigner la nouvelle position au robot.
    robot_modifier_position(robot, nouvelle_position)


def robot_modifier_direction(robot, nouvelle_direction):
    """
    Modifie la direction du robot.

    Arguments:
        robot {dict}: robot.
        nouvelle_direction (float): nouvelle direction du robot (en rad).

    Retour :
        Rien.
    """

    robot['direction'] = nouvelle_direction


def robot_rectifier_direction(robot):
    """
    Rectifie la direction du robot.

    Arguments:
        robot {dict}: robot

    Retour :
        Rien.
    """

    # Extraire la direction initiale.
    direction = robot_obtenir_direction(robot)

    # Rectifier la direction.
    if direction >= 2 * pi:
        direction -= (2 * pi)

    elif direction < 0:
        direction += 2 * pi

    # Stocker la nouvelle position.
    robot_modifier_direction(robot, direction)


def robot_mise_a_jour_direction(robot, en_contact):
    """
    Met à jour le robot.

    Arguments:
        robot {dict} : robot.
        en_contact (bool) : indicateur de contact du robot.

    Retour :
        Rien.
    """

    # Calculer la nouvelle direction.
    direction_nouvelle = robot_obtenir_direction(robot) + normal(scale=DEVIATION_MOUVEMENT_ALEATOIRE)

    # Faire demi-tour s'il y a un contact.
    if en_contact:
        direction_nouvelle += pi

    # Stoker la nouvelle direction.
    robot_modifier_direction(robot, direction_nouvelle)

    # Rectifier la nouvelle direction du robot.
    robot_rectifier_direction(robot)


