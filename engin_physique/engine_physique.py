
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

# Gestion des fichiers.
from interface_fichiers.interface_json import json_charger_environnement


def environnement_init(nom_fichier):
    """
    Initialise l'engin physique.

    Arguments:
        nom_fichier (str) : le nom du fichier qui contient l'environnement à charger.

    Retourne:
        (dict): l'environnement initialisé.
    """

    # Initialiser la liste.
    objets = []

    # Charger les objets du fichier json.
    for obj in json_charger_environnement(nom_fichier):

        # Identifier le type de la forme.
        nom_de_la_Forme = obj["forme"]

        # Si le nom_de_la_forme est rectangle :
        if nom_de_la_Forme == "rectangle":
            objets.append(rectangle_init(obj['x'], obj['y'], obj['largeur'], obj['hauteur']))

        # Si le nom_de_la_Forme est cercle :
        if nom_de_la_Forme == "cercle".lower():
            objets.append(cercle_init(obj['x'], obj['y'], obj['rayon']))

    # Retourner le dictionnaire.
    return {'objets': objets}


def environnement_obtenir_objets(environnement):
    """
    Accède aux objets de l'environnement.

    Arguments :
        environnement (dict): l'environnement.

    Retourne:
        (list): liste d'objets de l'environnement.
    """

    return environnement['objets']


def robot_en_contact(environnement, robot):
    """
    Détermine les robots sont en contact.

    Arguments :
    environnement {dict}: l'environnement.
    les robots

    Retourne:
        (bool) : retourne si les robots sont en contact ou non.
    """

    # Indicateur de contact.
    est_contact = False

    # Calculer la prochain position.
    prochaine_position = robot_obtenir_prochaine_position(robot)

    # Extraire les composants de la prochaine position.
    x_prochain = position_obtenir_x(prochaine_position)
    y_prochain = position_obtenir_y(prochaine_position)

    # Initialiser un cercle(i.e un collisionneur) à la prochaine position du robot.
    collisionneur = cercle_init(x_prochain, y_prochain, robot_obtenir_rayon(robot))

    # Déterminer si contact avec quelconque obstacle.
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
