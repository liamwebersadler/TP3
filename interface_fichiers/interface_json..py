
from engin_physique.engin_physique import environnement_init
from configuration.constantes import FORME_CERCLE
from configuration.constantes import FORME_RECTANGLE


def creation_fichier():
    """
        Génération d'un fichier d'environnement.

        Arguments:
            Aucun.

        Retourne:
            Riens. TODO est ce que nous devons créé un fichier et ajouter l'environnement ou ajouter l'environnement dans un fichier deja créé
    """
    
    # Initialiser un environnement.
    environnement = environnement_init()

    # TODO a ou w
    with open("..\\{NOM_FICHIER_INTERFACE_FICHIERS}\\{NOM_FICHIER_EXEMPLES}\\{piece_avec_obstacles}", 'w') as fichier:

        # Parcourir les lignes du dictionnaire de chaque objet.
        for ligne in environnement['objets']:

            # Si la clé est de type cercle :
            if ligne['forme'] == FORME_CERCLE:

                # Déterminer les paramètres du cercle.
                x = ligne['x']
                y = ligne['y']
                rayon = ligne['rayon']
                forme = ligne['forme']

                # Ajouter la string au fichier.
                fichier.write(f'\'x\': {x}, \'y\': {y}, \'rayon\': {rayon}, \'forme\': {forme}')

            # Si la clé est de type rectangle :
            elif ligne['forme'] == FORME_RECTANGLE:

                # Déterminer les paramètres du rectangle.
                x = ligne['x']
                y = ligne['y']
                largeur = ligne['largeur']
                hauteur = ligne['hauteur']
                forme = ligne['forme']

                # Ajouter la string au fichier.
                print(f'\'x\': {x}, \'y\': {y}, \'largeur\': {largeur}, \'hauteur\': {hauteur}, \'forme\': {forme}')


creation_fichier()
#def json_charger(fichier):
   # with open('obstacles', 'w') as obstacle:


# return {'x': x, 'y': y, 'largeur': largeur, 'hauteur': hauteur, 'forme': FORME_RECTANGLE}
# return {'x': x, 'y': y, 'rayon': rayon, 'forme': FORME_CERCLE}


#def importer_manuels(nom_fichier):
    # Initialisations
   # liste_manuels = []
   # dict_manuels = dict()

    # Ingérer le fichier
    # fichier = open(nom_fichier)
    # liste_manuels = fichier.readlines()
    # fichier.close()

    # Convertir en dictionnaire
    # for i in range(len(liste_manuels)):
        # temp = liste_manuels[i].strip('\n')
        # titre, ISBN10 = temp.split(',')
        # dict_manuels[ISBN10] = titre

    # return dict_manuels


# Exemple d'exécution
# importer_manuels('manuels.txt')


def vecteur_liste_afficher(liste_vecteurs):
    for i in range(len(liste_vecteurs)):

        # Extraire les composants du vecteur
        dx = liste_vecteurs[i]['dx']
        dy = liste_vecteurs[i]['dy']
        longueur = liste_vecteurs[i]['longueur']

        # Afficher le vecteur avec ou sans longueur selon le cas
        if longueur is not None:
            print(f'Vecteur no.{i + 1}:\n\n\tdx = {dx}\n\tdy = {dy}\n\tlongueur = {longueur:.2f}\n')
        else:
            print(f'Vecteur no.{i + 1}:\n\n\tdx = {dx}\n\tdy = {dy}\n')