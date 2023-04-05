
# Constantes du programme.
from configuration.constantes import FORME_CERCLE
from configuration.constantes import FORME_RECTANGLE
from engin_physique.physique.Position import position_obtenir_x, position_obtenir_y

# Gestion du robot.
from engin_physique.robot.robot import robot_obtenir_prochaine_position
from engin_physique.robot.robot import robot_obtenir_rayon

# Gestion des obstacles.
from engin_physique.objets import objet_obtenir_forme

# Gestion des contacts
from engin_physique.objets.cercle import cercle_en_contact_avec_rectangle
from engin_physique.objets.cercle import cercle_contact_avec_cercle

# Gestion des positions.
from engin_physique.objets.cercle import cercle_init
from engin_physique.objets.rectangle import rectangle_init

def environnement_init():
    """
    Initialise l'engin physique.

    Arguments:
        nom_fichier (str) : le nom du fichier qui contient l'environnement à charger.

    Retourne:
        (dict): l'environnement initialisé.
    """

    # Ajouter des murs et un obstacle en forme de cercle.
    objets = [rectangle_init(12, 12, 0.1, 6),
              rectangle_init(18, 12, 0.1, 6),
              rectangle_init(12, 12, 6, 0.1),
              rectangle_init(12, 18, 6, 0.1),
              cercle_init(17, 17, 0.1)]

    return {'objets': objets}


def environnement_obtenir_objets(environnement):
    """
    Accède aux objets de l'environnement.

    Arguments :
        environnement (dict): L'envirionnement.

    Retourne:
        (list): Liste d'objets de l'environnement.
    """

    return environnement['objets']


def robot_en_contact(environnement, robot):

    # Indicateur de contact.
    est_contact = False

    # Calculer la prochain position.
    prochaine_position = robot_obtenir_prochaine_position(robot)

    # Extraire les composants de la prochaine position.
    x_prochain = position_obtenir_x(prochaine_position)
    y_prochain = position_obtenir_y(prochaine_position)

    # Initialiser un cercle(i.e un collisionneur) à la prochaine position du robot.
    collisionneur = cercle_init(x_prochain, y_prochain, robot_obtenir_rayon(robot))

    # Déterminer si contact avec quelconque obstacle
    for obstacle in environnement_obtenir_objets(environnement):

        # Gérer les contacts pour les différentes formes d'obstacles.
        if objet_obtenir_forme(obstacle) == FORME_CERCLE:
            est_contact = cercle_contact_avec_cercle(collisionneur, obstacle)

        elif objet_obtenir_forme(obstacle) == FORME_RECTANGLE:
            est_contact = cercle_en_contact_avec_rectangle(collisionneur, obstacle)

        # Signaler qu'il y a eu un contact.
        if est_contact:
            return True

    # Signaler qu'il n'y a pas eu de contact.
    return False
