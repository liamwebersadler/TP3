from engin_physique.engin_physique import environnement_init

from engin_simulation.engin_simulation import ROUTINES


def programme_principal():
    """
    Lance une simulation

    Arguments :
        Aucuns.

    Retourne:
        Rien.
    """

    # initialise le robot et charge l'enginPhysique
    environnement = environnement_init()

    # sélectionne la routine
    routine = ROUTINES.get("TEMPS_REEL", None)

    robot = None

    # lance la simulation
    if routine is not None:
        routine(environnement, robot)

    pass


if __name__ == "__main__":
    programme_principal()
