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

    # Initialiser le robot et charge l'enginPhysique.
    environnement = environnement_init()

    # Sélectionner la routine.
    routine = ROUTINES.get("TEMPS_REEL", None)

    robot = None

    # Lancer la simulation.
    if routine is not None:
        routine(environnement, robot)

    pass


if __name__ == "__main__":
    programme_principal()
