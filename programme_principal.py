# Importer les constantes du projet
from configuration.constantes import STRATEGIE_ALEATOIRE


from engin_physique.engin_physique import environnement_init
from engin_simulation.engin_simulation import ROUTINES

# Sous-programmes relatifs au robot
from engin_physique.robot.robot import robot_init


def programme_principal():
    """
    Lance une simulation

    Arguments :
        Aucuns.

    Retourne:
        Rien.
    """

    # Initialiser environment du robot
    environnement = environnement_init()

    # Initialiser un robot avec une stratégie aléatoire
    robot = robot_init(STRATEGIE_ALEATOIRE)

    # Sélectionner la routine.
    routine = ROUTINES.get("TEMPS_REEL", None)

    # Lancer la simulation.
    if routine is not None:
        routine(environnement, robot)

    pass


if __name__ == "__main__":
    programme_principal()
