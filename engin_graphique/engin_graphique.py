
# Fonctions importées
from matplotlib import animation
import matplotlib.pyplot as plt
from configuration.constantes import ROBOT_RAYON


class Vue():

    def init_animation(vue):
        """
        Initialise l'engin graphique.

        Arguments:
            vue (class): référence à la classe.

        Retourne:
            (patch): référence robot vue (inutilisé, mais requis par le module animation).
        """

        if vue.robot is not None:
            vue.robot_vue.center = (vue.robot["position"]["x"], vue.robot["position"]["y"])
        else:
            vue.robot_vue.center = (15, 15)

        vue.ax.add_patch(vue.robot_vue)

        for objet in vue.objets_vue:
            vue.ax.add_patch(objet)

        return vue.robot_vue,

    def animate(vue, i):
        """
        Anime les éléments de la simulation

        Arguments :
            vue (class): référence à la classe
            i (int) : numéro de frame envoyé par Animation (inutilisé).

        Retourne:
            (patch): référence robot vue (inutilisé, mais requis par le module animation).
        """

        from engin_simulation.engin_simulation import mise_a_jour_simulation

        # La simulation est silencieuse. Cette gestion des exceptions assure de les
        # afficher dans la console.
        try:
            mise_a_jour_simulation(vue.environnement, vue.robot)

            if vue.robot is not None:
                vue.robot_vue.center = (vue.robot["position"]["x"], vue.robot["position"]["y"])

        except Exception as e:
            print(e)

        return vue.robot_vue,


def init_vue(robot, environnement):
    """
    Initialise la vue en y attachant les références aux éléments de la simulation
    et initialise leur contre-parti visuel.

    Arguments:
        robot (robot): référence au robot.
        environnement (environnement) : référence à l'environnement.

    Returns :
        référence à la vue initialisée
    """

    vue = Vue()

    # Cette gestion permet aux étudiants de lancer la simulation avant que le robot
    # ne soit effectivement créé.
    if robot is not None:
        vue.robot = robot
        vue.robot_vue = plt.Circle((robot["position"]["x"], robot["position"]["y"]),
                                   ROBOT_RAYON, fc='y')
    else:
        vue.robot = None
        vue.robot_vue = plt.Circle((15, 15), ROBOT_RAYON, fc='y')

    vue.environnement = environnement

    # Lancer et configurer la fenêtre.
    vue.fig = plt.figure()
    vue.fig.set_dpi(100)
    vue.fig.set_size_inches(7, 6.5)

    vue.ax = plt.axes(xlim=(0, 30), ylim=(0, 30))

    vue.objets_vue = []

    # Créer les obstacles de l'environnement.
    for objet in vue.environnement["objets"]:
        if objet["forme"] == "cercle":
            vue.objets_vue.append(plt.Circle((objet["x"], objet["y"]),
                                  objet["rayon"], fill=True, color='k'))
        elif objet["forme"] == "rectangle":
            vue.objets_vue.append(plt.Rectangle((objet["x"], objet["y"]),
                                  objet["largeur"], objet["hauteur"],
                                  fill=True, color='k'))

    return vue


def lancer_animation(vue):
    """
    Lance la simulation et la fenêtre. Cet appel est bloquant.

    Arguments:
        vue (Vue): référence à la vue.

    Returns :

    """

    anim = animation.FuncAnimation(vue.fig,
                                   vue.animate,
                                   init_func=vue.init_animation,
                                   frames=100,
                                   interval=1,
                                   blit=True)
    plt.show()


def visualiser(vue, afficher = True):
    """
    Permet d'afficher la vue en dehors du cadre de l'animation

    Arguments :
        vue (vue): référence à la vue.

    Returns :

    """
    vue.init_animation()

    if afficher:
        plt.show()
