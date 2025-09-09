#importation modules
import numpy as np               # alias
import matplotlib.pyplot as plt  # alias

#definition maillage x
x=np.linspace(0,10,100)

#calcul de la fonction 
y=x*np.exp(-x)

#definition de la figuree
plt.figure(0)

#effacement de la figure
plt.clf()

#affichage de la grille
plt.grid(True)

#trace de la courbe
#--> couleur 
# noire :k
# bleu  :b
# jaune :y
# cyan  :c
# vert  :g
# rouge :r
#--> symbole
# - : trait continu
# o : chaque point de la courbe est un petit point noir par defaut
# --: trait interrompu court
# .-: alternance . et trait
plt.plot(x,y,'b-')

#definition legende suivant x
plt.xlabel(r'$x$')

#definition legende suivant y
plt.ylabel(r'$y$')

#specification de la zone d'affichage
plt.xlim((-0.25,10.25)) # syuvant x

#titre de la figure
plt.title('graphe de $y=x e^{-x}$ sur $[0,10]$')

#sauvegarde de l'image au format png
#avec une resolution de 400 dpi i.e. de 400 points par pouce(inch)
plt.savefig('expo.png',dpi=400)

