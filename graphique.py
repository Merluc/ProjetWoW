import cng
import avions as cls
import trajectoires as trj
import degats as dgt
import wow
from time import *
import math
import consts


def switch_color(id, color):
    """Change la couleur de l'objet en paramètre de la couleur en paramètre
    """
    # changement de la couleur courante
    cng.current_color(color)
    # changement de la couleur de l'objet
    cng.obj_put_color(id)


idb1 = 0
idb2 = 0


def health(P):
    """Affiche la jauge de vie de l'avion en paramètre de la taille et de la
    couleur adéquate en fonction de la vie restante
    """
    global max_p1, max_p2, idb1, idb2
    # nous vérifions si l'avion est le joueur 1 ou 2
    # et prenons les valeurs en conséquence
    if consts.P1.id == P.id:
        max_p = max_p1
        coord = 172.5
    else:
        max_p = max_p2
        coord = 1122.5
    # création des valeurs pour la taille de la jauge de vie en fonction
    # de la vie restante de l'avion
    p = P.health[0] * 100 / max_p
    h = 55 / 100 * p
    # choix de la couleur de la jauge en fonction de la vie restante
    if p >= 70:
        cng.current_color("green")
    elif p >= 40:
        cng.current_color("orange")
    else:
        cng.current_color("red")
    # suppresion de l'ancienne jauge et création de la nouvelle en fonction de
    # l'avion
    if consts.P1.id == P.id:
        if idb1:
            cng.obj_delete(idb1)
        idb1 = cng.box(coord, 42.5, coord + h, 17.5)
    else:
        if idb2:
            cng.obj_delete(idb2)
        idb2 = cng.box(coord, 42.5, coord + h, 17.5)


def kill(P, cause):
    """Efface l'avion en paramètre en affichant son lieu de mort et affiche la
    victoire de l'avion restant avec l'explication de la mort.
    """
    global imgDe, idb1, idb2
    # mise a jour de la couleur courante en noir
    cng.current_color("black")
    # sélection du texte à afficher en fonction de la raison de mort
    if cause == "o":
        cause = "ADVERSAIRE HORS ZONE"
    elif cause == "d":
        cause = "AVION ADVERSE DÉTRUIT"
    else:
        cause = "PILOTE ADVERSE MORT"
    P.health[0] = 0
    # affichage de l'emplacement de mort avec une image
    imgDe = cng.image("mort.png", 50, 50)
    idDe = cng.image_draw(P.pos[0], 1000 - P.pos[1], imgDe)
    # affichage du texte de victoire et de la mort de l'autre avion
    if P.id == consts.P1.id:
        cng.obj_delete(idb1)
        cng.text(540, 30, "VICTOIRE P2")
        cng.text(500, 10, cause)
    else:
        cng.obj_delete(idb2)
        cng.text(540, 30, "VICTOIRE P1")
        cng.text(500, 10, cause)
    # suppression de l'avion mort
    cng.obj_delete(P.id)
    cng.refresh()
    sleep(10)
    exit()


def pilote(P):
    """Affiche graphiquement quand le pilote de l'avion en paramètre à été
    touché.
    """
    # mise a jour de la couleur courante en rouge
    cng.current_color("red")
    # affichage de l'indication du pilote bléssé en fonction de l'avion
    if P.id == consts.P1.id:
        cng.text(235, 20, "PILOTE BLÉSSÉ")
    else:
        cng.text(1185, 20, "PILOTE BLÉSSÉ")


def explo(P):
    """Affiche l'explosion sur l'avion en paramètre qui à été touché
    """
    global imgEx, idex
    # affichage de l'image de l'explosion sur l'avion touché
    imgEx = cng.image("explo.png", 50, 50)
    idex = cng.image_draw(P.pos[0], 1000 - P.pos[1], imgEx)


idex = 0


def move():
    """Appelle les trajectoires souhaitées par les joueurs et récupère les
    listes de points générés pour les éffectuer simultanéments pour les deux
    avions.
    """
    global idex
    # si les deux joueurs ont bien sélectionnés leurs 3 actions
    if len(act_p1) == 3 and len(act_p2) == 3:
        # pour chacune de ces actions
        for i in range(3):
            liste = []
            # on récupère la iste de points en fonction de l'action souhaitée
            # pour l'avion 1
            if act_p1[i] == 'a':
                liste += trj.tourner_gauche(consts.P1)
            elif act_p1[i] == 'e':
                liste += trj.tourner_droit(consts.P1)
            elif act_p1[i] == 'z':
                liste += trj.tout_droit(consts.P1)
            elif act_p1[i] == 'd':
                liste += trj.glissement_droit(consts.P1)
            elif act_p1[i] == 'q':
                liste += trj.glissement_gauche(consts.P1)
            # pour l'avion 2
            if act_p2[i] == 'i':
                liste += trj.tourner_gauche(consts.P2)
            elif act_p2[i] == 'p':
                liste += trj.tourner_droit(consts.P2)
            elif act_p2[i] == 'o':
                liste += trj.tout_droit(consts.P2)
            elif act_p2[i] == 'm':
                liste += trj.glissement_droit(consts.P2)
            elif act_p2[i] == 'k':
                liste += trj.glissement_gauche(consts.P2)
            # initialisation des flags de tir
            flag_shoot1 = 0
            flag_shoot2 = 0
            # pour chacun des mouvements éffectués
            for p in range(len(liste[0])):
                # on vérifie si l'avion à déjà tiré durant cette manoeuvre
                # si non on regarde si cela est possible
                if not flag_shoot1:
                    flag_shoot1 = dgt.in_range(consts.P1)
                if not flag_shoot2:
                    flag_shoot2 = dgt.in_range(consts.P2)
                # on fait bouger les deux avions en fonction des
                # coordonnées de leur liste respective
                cng.obj_put_coord(consts.P1.id, [liste[0][p][0],
                                  liste[0][p][1]])
                cng.obj_put_coord(consts.P2.id, [liste[2][p][0],
                                  liste[2][p][1]])
                # on fait tourner les deux avions en fonction de leur
                # mouvement respectif
                consts.P1.id = cng.image_rotate(consts.P1.pic, consts.P1.id,
                                                -consts.P1.dir + liste[1][p])
                consts.P2.id = cng.image_rotate(consts.P2.pic, consts.P2.id,
                                                -consts.P2.dir + liste[3][p])
                # maj de la pos de l'avion dans sa classe
                consts.P1.pos = [liste[0][p][0], 1000 - liste[0][p][1]]
                consts.P2.pos = [liste[2][p][0], 1000 - liste[2][p][1]]
                cng.refresh()
                sleep(0.01)
            # maj de l'orientation de l'avion en fonction de sa manoeuvre
            consts.P1.dir += -liste[1][-1]
            consts.P2.dir += -liste[3][-1]
            # suppresion de l'image d'explosion à la fin de la manoeuvre
            if idex:
                cng.obj_delete(idex)
        # on vérifie si les avions sont toujours dans la zone de jeu
        dgt.plan()
        # on réinitialise les listes d'actions
        reset()


def reset():
    """Réinitialise les listes d'actions demandés par les joueurs.
    """
    global Lact, Ract, act_p1, act_p2
    # on reinitialise graphiquement les actions
    for i in Lact:
        switch_color(i, "white")
    for i in Ract:
        switch_color(i, "white")
    # on réinitialise les listes d'actions
    act_p1, act_p2 = [], []


def init_win():
    """Initialise la fenêtre graphique.
    """
    global fond, Lact, Ract
    # Initialisation fenêtre
    cng.init_window("Planes", 1325, 1000)
    # création de l'image de fond'
    fond = cng.image("photo_aerienne.jpg", 1550, 900)
    cng.image_draw(670, 550, fond)
    # initialisation des indicateurs graphique des actions du joueur 1
    L0 = cng.circle(30, 30, 20)
    L1 = cng.circle(75, 30, 20)
    L2 = cng.circle(120, 30, 20)
    # initialisation de la liste d'action du joueur 1
    Lact = [L0, L1, L2]
    # initialisation de la jauge de vie du joueur 1
    cng.rectangle(170, 45, 230, 15, pep=5)
    # initialisation des indicateurs graphique des actions du joueur 2
    R0 = cng.circle(980, 30, 20)
    R1 = cng.circle(1025, 30, 20)
    R2 = cng.circle(1070, 30, 20)
    # initialisation de la liste d'action du joueur 2
    Ract = [R0, R1, R2]
    # initialisation de la jauge de vie du joueur 2
    cng.rectangle(1120, 45, 1180, 15, pep=5)


def init_pl():
    """Initialise graphiquement les avions des joueurs.
    """
    global imgP1, imgP2, max_p1, max_p2
    # création de l'image du joueur 1
    imgP1 = cng.image(consts.P1.pic, 50, 50)
    id1 = cng.image_draw(150, 150, imgP1)
    # maj des données de la classe du joueur 1
    consts.P1.pic = imgP1
    consts.P1.pos = [150, 1000 - 150]
    consts.P1.id = id1
    max_p1 = consts.P1.health[0]
    health(consts.P1)
    # création de l'image du joueur 2
    imgP2 = cng.image(consts.P2.pic, 50, 50)
    id2 = cng.image_draw(1175, 950, imgP2)
    # maj des données de la classe du joueur 2
    consts.P2.pic = imgP2
    consts.P2.pos = [1175, 1000 - 950]
    consts.P2.id = id2
    consts.P2.id = cng.image_rotate(consts.P2.pic, consts.P2.id, 180)
    consts.P2.dir = 180
    max_p2 = consts.P2.health[0]
    health(consts.P2)


def actions():
    """Enregistre les actions demandées par les joueurs et l'affiche
    graphiquement.
    """
    global P1A, Lact, P2A, Ract, act_p1, act_p2
    # on regarde à quelle liste appartient la touche préssée
    if cng.get_key() in ['a', 'e', 'z', 'd', 'q']:
        # on vérifie si le joueur à pas déja rentré 3 actions
        if len(act_p1) < 3:
            # on change l'indicateur graphique, le compteur et la
            # liste d'actions
            switch_color(Lact[P1A], "green")
            P1A = (P1A + 1) % 3
            act_p1 += [cng.get_key()]
    elif cng.get_key() in ['i', 'p', 'o', 'm', 'k']:
        # on vérifie si le joueur à pas déja rentré 3 actions
        if len(act_p2) < 3:
            # on change l'indicateur graphique, le compteur et la
            # liste d'actions
            switch_color(Ract[P2A], "green")
            P2A = (P2A + 1) % 3
            act_p2 += [cng.get_key()]
    elif cng.get_key() in ['&', 'é', '"', "'", 'r', 'f', 'v', 'c', 'x',
                           'w', 's']:
        # on vérifie si le joueur à pas déja rentré 3 actions
        if len(act_p1) < 3:
            # on change l'indicateur graphique pour indiquer la mauvaise saisie
            switch_color(Lact[P1A], "red")
            cng.refresh()
            sleep(0.8)
            switch_color(Lact[P1A], "white")
    elif cng.get_key() in ['è', '_', 'ç', 'à', ')', '^', 'ù', '!', ':', 'l',
                           ';', ',', 'j', 'u']:
        # on vérifie si le joueur à pas déja rentré 3 actions
        if len(act_p2) < 3:
            # on change l'indicateur graphique pour indiquer la mauvaise saisie
            switch_color(Ract[P2A], "red")
            cng.refresh()
            sleep(0.8)
            switch_color(Ract[P2A], "white")

act_p1 = []
act_p2 = []
P1A = 0
P2A = 0
