"""
Ce fichier défini les modes d'opérations (routines). Par souci d'abstraction, toutes les routines
présentent la même liste de paramètres, même si les paramètres ne sont pas nécessairement utilisés.

Les routines qui simulent le système appellent mise_a_jour_simulation directement ou via l'animation
"""

# Gestion du mode de la vue.
from engin_graphique.engin_graphique import init_vue
from engin_graphique.engin_graphique import lancer_animation
from engin_graphique.engin_graphique import visualiser

# Gestion du mode de la routine.
from configuration.constantes import OPTION_TEMPS_REEL
from configuration.constantes import OPTION_VISUALISER

# Gestion des collisions.
from engin_physique.engin_physique import robot_en_contact

# Fonctions de gestion du robot.
from engin_physique.robot.robot import robot_effectuer_deplacement
from engin_physique.robot.robot import robot_mise_a_jour_direction


def mise_a_jour_simulation(environnement, robot):
    """
    Sous-programme qui simule une itération :
        * Déterminer s'il y a contact avec un objet de l'environnement
        * Mettre à jour le système de décision du robot
        * Si pas en contact, faire le déplacement

    Arguments :
        environnement (dict): L'environnement du robot.
        robot (dict): Le robot.

    """

    # Déterminer s'il y a un contact avec l'un des obstacles de l'environnement.
    en_contact = robot_en_contact(environnement, robot)

    # Mettre le robot à jour (c'est-à-dire la direction).
    robot_mise_a_jour_direction(robot, en_contact)

    # Déplacer le robot.
    if not en_contact:
        robot_effectuer_deplacement(robot)


def simul_temps_reel(environnement, robot=None):
    """
    Routine qui simule en temps réel et présente la simulation à l'écran.

    À la fin de la simulation, la carte de chaleur est présentée.

    :param robot: référence au robot-aspirateur.
    :param environnement: référence à l'enginPhysique.
    """

    vue = init_vue(robot, environnement)
    lancer_animation(vue)


ROUTINES = {"TEMPS_REEL": simul_temps_reel}


def simulation_visualiser_environnement(environnement, robot):

    # Créer la vue.
    vue = init_vue(robot, environnement)

    # Afficher l'environnement sans lancer la simulation.
    visualiser(vue)


ROUTINES = {OPTION_TEMPS_REEL: simul_temps_reel,
            OPTION_VISUALISER: simulation_visualiser_environnement}

