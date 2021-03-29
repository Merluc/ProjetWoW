import numpy as np
import graphique as gr
import consts
import math
import matplotlib.pyplot as plt

#######################################################################
# génère les points pour former une courbe de bézier


def curve(t_values, points):
    """Retourne la liste de point qui forme la courbe de Bézier.
    """
    curve = []
    for t in t_values:
        curve += [Point(t, points)]
    return curve


def Point(t, points):
    """Retourne un point fait avec la méthode de Bézier.
    """
    newpoints = points
    while len(newpoints) > 1:
        newpoints = Points(t, newpoints)
    return newpoints[0]


def Points(t, points):
    """Retourne une liste de points fait avrec la méthode de Bézier.
    """
    newpoints = []
    for i in range(len(points) - 1):
        newpoints += [Twopoints(t, points[i], points[i + 1])]
    return newpoints


def Twopoints(t, P1, P2):
    """Retourne un point entre P1 et P2 en fonction de t.
    """
    Q1 = []
    Q1 += [(1 - t) * P1[0] + t * P2[0]]
    Q1 += [(1 - t) * P1[1] + t * P2[1]]
    return Q1


#######################################################################
# création de trajectoires en fonction d'un objet P.
def rotate_coord(coord, P):
    """Retourne les coordonnées en paramètre en fonction
    de la direction de P.
    """
    # on récupère la direction de l'avion en radians
    angle = math.radians(P.dir)
    new_coord = []
    # on applique la rotation sur toute les coordonnées
    for i in coord:
        rotation_x = i[0] * math.cos(angle) + i[1] * math.sin(angle)
        rotation_y = i[1] * math.cos(angle) - i[0] * math.sin(angle)
        new_coord += [[rotation_x, rotation_y]]
    # on retourne les nouvelles coordonnées
    return new_coord


def tout_droit(P):
    """Retourne une liste de points formant une courbe de Bézier allant tout
    droit en fonction de la position et direction de P.
    """
    # points de controle pour Bézier en fonction de la vitesse de l'avion
    po = [[0, 0], [0, 20 * P.speed], [0, 30 * P.speed], [0, 50 * P.speed]]
    # on ajuste les points de controle en fonction de la direction
    no = rotate_coord(po, P)
    # on ajuste les points de controle en fonction de la position actuelle
    test = [[P.pos[0], 1000 - P.pos[1]], [P.pos[0], 1000 - P.pos[1] +
            no[1][1]], [P.pos[0] + no[2][0], 1000 - P.pos[1] + no[2][1]],
            [P.pos[0] + no[3][0], 1000 - P.pos[1] + no[3][1]]]
    # on applique Bézier avec ces points de controle
    test_set_1 = curve(consts.t_points, test)
    flag_shoot = 0
    return [test_set_1, consts.tn]


def glissement_droit(P):
    """Retourne une liste de points formant une courbe de Bézier formant un
    glissement à droite en fonction de la position et direction de P.
    """
    # points de controle pour Bézier en fonction de la vitesse de l'avion
    po = [[0, 0], [0, 50 * P.speed], [50 * P.speed, 50 * P.speed],
          [50 * P.speed, 100 * P.speed]]
    # on ajuste les points en fonction de la direction
    no = rotate_coord(po, P)
    # on ajuste les points de controle en fonction de la position actuelle
    test = [[P.pos[0], 1000 - P.pos[1]], [P.pos[0], 1000 - P.pos[1] +
            no[1][1]], [P.pos[0] + no[2][0], 1000 - P.pos[1] + no[2][1]],
            [P.pos[0] + no[3][0], 1000 - P.pos[1] + no[3][1]]]
    # on applique Bézier avec ces points de controle
    test_set_1 = curve(consts.t_points, test)
    return [test_set_1, consts.tn]


def glissement_gauche(P):
    """Retourne une liste de points formant une courbe de Bézier formant un
    glissement à gauche en fonction de la position et direction de P.
    """
    # points de controle pour Bézier en fonction de la vitesse de l'avion
    po = [[0, 0], [0, 50 * P.speed], [-50 * P.speed, 50 * P.speed],
          [-50 * P.speed, 100 * P.speed]]
    # on ajuste les points en fonction de la direction
    no = rotate_coord(po, P)
    # on ajuste les points de controle en fonction de la position actuelle
    test = [[P.pos[0], 1000 - P.pos[1]], [P.pos[0], 1000 - P.pos[1] +
            no[1][1]], [P.pos[0] + no[2][0], 1000 - P.pos[1] + no[2][1]],
            [P.pos[0] + no[3][0], 1000 - P.pos[1] + no[3][1]]]
    # on applique Bézier avec ces points de controle
    test_set_1 = curve(consts.t_points, test)
    return [test_set_1, consts.tn]


def tourner_droit(P):
    """Retourne une liste de points formant une courbe de Bézier formant un
    virage à droite en fonction de la position et direction de P.
    """
    # points de controle pour Bézier en fonction de la vitesse de l'avion
    po = [[0, 0], [0, 20 * P.speed], [10 * P.speed, 30 * P.speed],
          [30 * P.speed, 30 * P.speed]]
    # on ajuste les points en fonction de la direction
    no = rotate_coord(po, P)
    # on ajuste les points de controle en fonction de la position actuelle
    test = [[P.pos[0], 1000 - P.pos[1]], [P.pos[0], 1000 - P.pos[1] +
            no[1][1]], [P.pos[0] + no[2][0], 1000 - P.pos[1] + no[2][1]],
            [P.pos[0] + no[3][0], 1000 - P.pos[1] + no[3][1]]]
    # on applique Bézier avec ces points de controle
    test_set_1 = curve(consts.t_points, test)
    return [test_set_1, consts.td]


def tourner_gauche(P):
    """Retourne une liste de points formant une courbe de Bézier formant un
    virage à gauche en fonction de la position et direction de P.
    """
    # points de controle pour Bézier en fonction de la vitesse de l'avion
    po = [[0, 0], [0, 20 * P.speed], [-10 * P.speed, 30 * P.speed],
          [-30 * P.speed, 30 * P.speed]]
    # on ajuste les points en fonction de la direction
    no = rotate_coord(po, P)
    # on ajuste les points de controle en fonction de la position actuelle
    test = [[P.pos[0], 1000 - P.pos[1]], [P.pos[0], 1000 - P.pos[1] +
            no[1][1]], [P.pos[0] + no[2][0], 1000 - P.pos[1] + no[2][1]],
            [P.pos[0] + no[3][0], 1000 - P.pos[1] + no[3][1]]]
    # on applique Bézier avec ces points de controle
    test_set_1 = curve(consts.t_points, test)
    return [test_set_1, consts.tg]


def test_unit():
    # test des fonctions pour les courbes de Bézier
    t_points = np.arange(0, 1, 0.001)
    test = a([[0, 0], [0, 2], [1, 3], [3, 4]])
    test_set_1 = curve(t_points, test)
    plt.plot(test_set_1[:, 0], test_set_1[:, 1])
    plt.plot(test[:, 0], test[:, 1], 'ro:')


if __name__ == "__main__":
    test_unit()
