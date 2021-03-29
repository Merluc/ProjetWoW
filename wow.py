import sys
import cng
import avions as cls
import graphique as gr
import consts
import degats as dgt
import math
import trajectoires as trj
from time import *


def players(pl1, pl2):
    """Initialise les deux avions en fonction des paramètres sélectionné.
    """
    # Initialisation P1
    if pl1 == "albatros":
        consts.P1 = cls.Albatros()
    elif pl1 == "fokker":
        consts.P1 = cls.Fokker()
    elif pl1 == "sopwith":
        consts.P1 = cls.Sopwith()
    else:
        consts.P1 = cls.Spad()

    # Initialisation P2
    if pl2 == "albatros":
        consts.P2 = cls.Albatros()
    elif pl2 == "fokker":
        consts.P2 = cls.Fokker()
    elif pl2 == "sopwith":
        consts.P2 = cls.Sopwith()
    else:
        consts.P2 = cls.Spad()


def vecteur(A, B):
    """Retourne un vecteur en fonction de deux points.
    """
    return (B[0] - A[0], B[1] - A[1])


def scalaire(U, V):
    """Retourne le produit scalaire en fonction de deux vecteurs.
    """
    return (U[0] * V[0] + U[1] * V[1])


def norme(V):
    """Retourne la norme du vecteur en paramètre.
    """
    return (math.sqrt((V[0] * V[0]) + (V[1] * V[1])))


def calcule_angle(A, B, C):
    """Retourne la valeur de l'angle A en degrés formé par BA AC.
    """
    V = vecteur(A, B)
    U = vecteur(A, C)
    return (math.degrees(math.acos(scalaire(U, V) / (norme(U) * norme(V)))))


def main_func():
    """Fonction lancant l'éxecution du jeu.
    """
    players(sys.argv[1], sys.argv[2])
    gr.init_win()
    gr.init_pl()
    cng.init_idle_func(gr.move)
    cng.idle_start()
    cng.idle_func()
    for c in ['a', 'e', 'z', 'd', 'q', 'i', 'p', 'o', 'm', 'k', '&', 'é', '"',
              "'", 'r', 'f', 'v', 'c', 'x', 'w', 's', 'è', '_', 'ç', 'à', ')',
              '^', 'ù', '!', ':', 'l', ';', ',', 'j', 'u']:
        cng.assoc_key(c, gr.actions)
    cng.main_loop()


def test_unit():
    A = (3, 3)
    B = (6, 3)
    C = (3, 6)

    U = vecteur(A, B)
    V = vecteur(A, C)
    print("U = ", U, "V = ", V)
    print("scalaire(U, V) = ", scalaire(U, V))
    print("norme(U) = ", norme(U), "norme(V) = ", norme(V))
    print("angle BAC = ", calcule_angle(A, B, C))


if __name__ == "__main__":
    main_func()
    # test_unit()
