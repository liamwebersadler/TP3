#from engin_physique.engine_physique import environnement_init
from configuration.constantes import FORME_CERCLE
from configuration.constantes import FORME_RECTANGLE
import json

"""
      Génération d'un fichier d'environnement.

      Arguments:
          Aucun.

      Retourne:
          Riens. TODO est ce que nous devons créé un fichier et ajouter l'environnement ou ajouter l'environnement dans un fichier deja créé
  """
"""
def creation_fichier():
  

    # Initialiser un environnement.
    #environnement = environnement_init()

    # TODO a ou w
    with open("..\\{NOM_FICHIER_INTERFACE_FICHIERS}\\{NOM_FICHIER_EXEMPLES}\\obstacles", 'w') as fichier:

        # Parcourir les lignes du dictionnaire de chaque objet.
        for ligne in environnement['objets']:

            # Si la clé est de type cercle :
            if ligne['forme'] == FORME_CERCLE:

                # Déterminer les paramètres du cercle.
                x = ligne['x']
                y = ligne['y']
                rayon = ligne['rayon']
                forme = ligne['forme']

                # Ajouter la chaine de caractère au fichier.
                fichier.write(f'\'x\': {x}, \'y\': {y}, \'rayon\': {rayon}, \'forme\': {forme}')

            # Si la clé est de type rectangle :
            elif ligne['forme'] == FORME_RECTANGLE:

                # Déterminer les paramètres du rectangle.
                x = ligne['x']
                y = ligne['y']
                largeur = ligne['largeur']
                hauteur = ligne['hauteur']
                forme = ligne['forme']

                # Ajouter la chaine de caractère au fichier.
                fichier.write(f'\'x\': {x}, \'y\': {y}, \'largeur\': {largeur}, \'hauteur\': {hauteur}, \'forme\': '
                              f'{forme}')
"""


def json_charger_environnement(fichier):

    with open(fichier, 'r') as environnement:
        texte = environnement.readlines()

    # Initialiser une liste.
    liste_obstacles = []

    # Parcourir les lignes du fichier.
    for ligne in texte:

        # Extraire les valeurs et les mettre dans la liste_obstacles.
        x = json.loads(ligne)
        liste_obstacles.append(x)

    # Retourner la liste.
    return liste_obstacles
