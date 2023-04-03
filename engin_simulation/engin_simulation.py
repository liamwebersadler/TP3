"""
Ce fichier défini les modes d'opérations (routines). Par souci d'abstraction, toutes les routines
présentent la même liste de paramètres, même si les paramètres ne sont pas nécessairement utilisés.

Les routines qui simulent le système appelent mise_a_jour_simulation directement ou via l'animation

"""

import os

import numpy as np
import matplotlib.pyplot as plt

from engin_graphique.engin_graphique import init_vue
from engin_graphique.engin_graphique import lancer_animation


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

    print("mise à jour de la simulation")


def simul_temps_reel(environnement, robot=None):
    """
    Routine qui simule en temps réel et présente la simulation à l'écran.

    À la fin de la simulation, la carte de chaleur est présentée.

    :param robot: référence au robot-aspirateur
    :param environnement: référence à l'enginPhysique
    """

    vue = init_vue(robot, environnement)
    lancer_animation(vue)


ROUTINES = {"TEMPS_REEL": simul_temps_reel}
