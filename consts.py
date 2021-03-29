import numpy as np
# avion joueur 1
P1 = 0
# avion joueur 2
P2 = 0
# liste pour determiner nombre de points dans les courbes de Bézier
t_points = np.arange(0, 1, 0.01)
# liste des rotations lorsqu'un avion tourne à gauche
tg = np.arange(0, 90, 90 / len(t_points))
# liste des rotations lorsqu'un avion tourne à droite
td = np.negative(np.arange(0, 90, 90 / len(t_points)))
# liste lorsque aucune rotation est nécessaire
tn = np.zeros(len(t_points))
