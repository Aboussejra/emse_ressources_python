import matplotlib.pyplot as plt
import numpy as np
#nombre de tours
index=2.0
#tableau des instants
t=np.linspace(0,2*index*pi,10000)
#equation polaire
r=cos(t/index)
#x(t)
x=cos(t)*r
#y(t)
y=sin(t)*r
#definition fenetre graphique
plt.figure()
#effacement ecran
plt.clf()
#trace de la courbe
plt.plot(x,y,'r')  
#label axe des y
plt.ylabel(r'$y$')
#label axe des x
plt.xlabel(r'$x$')
#affichage de la grille
plt.grid(True)
#plt.savefig("",dpi=400)
plt.show()

