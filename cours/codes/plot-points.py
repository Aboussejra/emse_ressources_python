#importation modules
import numpy as np
import matplotlib.pyplot as plt  # alias

data=np.loadtxt('./points.txt')

#definition de la figuree
plt.figure(0)

#effacement de la figure
plt.clf()

#affichage de la grille
plt.grid(True)

#trace du nuage de points
plt.plot(data[:,0],data[:,1],'ro-')

#definition legende suivant x
plt.xlabel(r'$x$')

#definition legende suivant y
plt.ylabel(r'$y$')

#sauvegarde de l'image au format png
#avec une resolution de 400 dpi i.e. de 400 points par pouce(inch)
plt.savefig('points.png',dpi=400)

