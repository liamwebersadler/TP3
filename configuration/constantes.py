from math import pi


'''
  Chemins / noms de fichiers
'''

# Nom du fichier qui contient l'interface JSON et les exemples
NOM_FICHIER_INTERFACE_FICHIERS = 'interface_fichiers'

# Nom du fichier qui contient les exemples JSON
NOM_FICHIER_EXEMPLES = 'exemples'

'''
 Constantes du programme.
'''

# État du menu.
MENU_ACTIF = True

# Stratégies de recherche.
STRATEGIE_ALEATOIRE = 'Aléatoire'
STRATEGIE_A_STAR = 'A*'

# Menu de stratégies de recherche.
MENU_STRATEGIES = {0: 'Aléatoire',
                   2: 'A*'}

# Modes de fonctionnement de l'application pour le menu.
OPTION_VISUALISER = 'VISUALISER_ENVIRONNEMENT'
OPTION_TEMPS_REEL = 'TEMPS REEL'

MENU_MODES_OPERATIONS = {0: OPTION_VISUALISER,
                         1: OPTION_TEMPS_REEL}

'''
 Constantes d'environnement.
'''

# Position de l'obstacle par défaut
OBSTACLE_X_DEFAUT = 0
OBSTACLE_Y_DEFAUT = 0

# Dimensions de l'obstacle par défaut
OBSTACLE_LARGEUR_DEFAUT = 100
OBSTACLE_HAUTEUR_DEFAUT = 100

# Obstacle par défaut
PIECE = {'haut-gauche': {'x': 0, 'y': 0},
         'largeur': OBSTACLE_LARGEUR_DEFAUT,
         'hauteur': OBSTACLE_LARGEUR_DEFAUT}

'''
 Constantes du robot
'''

# Encodage de la forme d'un cercle
FORME_CERCLE = "cercle"

# Encodage de la forme d'un rectangle
FORME_RECTANGLE = "rectangle"

'''
 Constantes du robot
'''

# Position initiale du robot.
ROBOT_X_INITIAL = 15
ROBOT_Y_INITIAL = 15

# Dimension du robot circulaire [m].
ROBOT_RAYON = 0.3

# Vitesse d'avance [m/s].
ROBOT_VITESSE_INITIALE = 0.1

# Direction [rad].
ROBOT_DIRECTION_INITIALE = 0

# Grandeur d'un changement de direction aléatoire [rad].
DEVIATION_MOUVEMENT_ALEATOIRE = pi/16
