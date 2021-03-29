import consts
import math
import graphique as gr
import trajectoires as trj
import wow
import random
import cng


def distance():
    """Retourne la distance entre les deux avions.
    """
    #  sqrt((xB – xA)2 +  (yB-yA)2)
    A = (consts.P2.pos[0] - consts.P1.pos[0]) * (consts.P2.pos[0] -
         consts.P1.pos[0])
    B = (consts.P2.pos[1] - consts.P1.pos[1]) * (consts.P2.pos[1] -
         consts.P1.pos[1])
    return math.sqrt(A + B)


def in_range(P):
    """Vérifie si l'avion en paramètre a dans son anngle de tir l'autre avion,
    si oui, appelle shoot() et retourne 1 sinon retourne 0.
    """
    # on regarde quel avion est en paramètre
    if P.id == consts.P1.id:
        # on regarde si la distance entre les deux avions est inferieur
        # a la portée de tir de l'avion
        if consts.P1.range >= distance():
            # création d'un point dans la direction  actuelle de l'avion
            face = trj.rotate_coord([[0, 1]], consts.P1)
            # calcul si l'avion est dans l'angle de tir
            if wow.calcule_angle(consts.P1.pos, [consts.P1.pos[0] + face[0][0],
                                 consts.P1.pos[1] - face[0][1]],
                                 consts.P2.pos) <= 45:
                # si oui on tir et on retourne 1
                shoot(consts.P2)
                return 1
    else:
        # on regarde si la distance entre les deux avions est inferieur
        # a la portée de tir de l'avion
        if consts.P2.range >= distance():
            # création d'un point dans la direction  actuelle de l'avion
            face = trj.rotate_coord([[0, 1]], consts.P2)
            # calcul si l'avion est dans l'angle de tir
            if wow.calcule_angle(consts.P2.pos, [consts.P2.pos[0] + face[0][0],
                                 consts.P2.pos[1] - face[0][1]],
                                 consts.P1.pos) <= 45:
                # si oui on tir et on retourne 1
                shoot(consts.P1)
                return 1
    return 0


def shoot(P):
    """Génère un nombre aléatoire et inflige ces dégats à l'avion en paramètre,
    tout en mettant à jour les informations graphiques.
    """
    # création d'une valeur aléatoire
    dammage = random.randrange(0, 11, 1)
    # si elle vaut 11 on inflige un dégat au pilote
    if dammage == 11:
        P.health[1] -= 1
        if P.health[1] <= 0:
            gr.kill(P, "p")
            return -1
        gr.pilote(P)
    else:
        # si la valeur vaut plus de 5 on divise par deux
        if dammage > 5:
            dammage /= 2
        P.health[0] -= dammage
        if P.health[0] <= 0:
            gr.kill(P, "d")
            return -1
    # on affiche graphiquement les degats et la nouvelle vie
    gr.explo(P)
    gr.health(P)


def plan():
    """Vérifie si les avions en paramètres sont toujours dans la zone de jeu,
    si non, appelle la fonction kill()
    """
    # on vérifie si l'avion 1 est encore dans la zone en x
    if consts.P1.pos[0] < 0 or consts.P1.pos[0] > 1325:
        gr.kill(consts.P1, "o")
    # on vérifie si l'avion 1 est encore dans la zone en y
    elif consts.P1.pos[1] < 0 or consts.P1.pos[1] > 900:
        gr.kill(consts.P1, "o")
    # on vérifie si l'avion 2 est encore dans la zone en x
    if consts.P2.pos[0] < 0 or consts.P2.pos[0] > 1325:
        gr.kill(consts.P2, "o")
    # on vérifie si l'avion 2 est encore dans la zone en y
    elif consts.P2.pos[1] < 0 or consts.P2.pos[1] > 900:
        gr.kill(consts.P2, "o")
