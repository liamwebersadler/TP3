# Importer les constantes du projet.
from configuration.constantes import STRATEGIE_ALEATOIRE, STRATEGIE_A_STAR
from configuration.constantes import MENU_ACTIF
from configuration.constantes import OPTION_VISUALISER
from engin_graphique.engin_graphique import init_vue, visualiser, lancer_animation
from engin_physique.engine_physique import environnement_init
from engin_simulation.engin_simulation import ROUTINES
from engin_simulation.engin_simulation import simulation_visualiser_environnement
from configuration.constantes import OPTION_TEMPS_REEL

# Sous-programmes relatifs au robot.
from engin_physique.robot.robot import robot_init

# Affichages du menu.
from menu_operation.menu import choisir_mode_operation
from menu_operation.menu import choisir_environnement
from menu_operation.menu import choisir_strategie_robot


def programme_principal():
    """
    Lance une simulation

    Arguments :
        Aucuns.

    Retourne:
        Rien.
    """

    if MENU_ACTIF:
        # Paramètres choisis par l'utilisateur
        mode = choisir_mode_operation()
        strategie = choisir_strategie_robot()
        environnement = choisir_environnement("./interface_fichiers/exemples")

    else:
        # Paramètres par défaut.
        mode = OPTION_TEMPS_REEL
        strategie = STRATEGIE_ALEATOIRE
        environnement = environnement_init('./interface_fichiers/exemples/piece_complexe.json')

    # Initialiser un robot avec une stratégie.
    robot = robot_init(strategie)

    # Gestion de l'animation.
    routine = ROUTINES.get(mode, None)

    if routine is not None:
        routine(environnement, robot)

    vue = init_vue(robot, environnement)

    visualiser(vue)
    lancer_animation(vue)


from math import pi
if __name__ == "__main__":
    programme_principal()
