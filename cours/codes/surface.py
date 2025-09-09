# -*- coding: utf-8 -*-
"""
Trace de surface z=f(x,y)
@author: aa
"""
#----------------------------
#chargement des bibliotheques
#----------------------------
from mpl_toolkits.mplot3d import *  # Axes3D
from matplotlib import cm           # Couleurs !
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()    # Fenêtre vide - conteneur
ax = Axes3D(fig)
X,Y = np.linspace(-2,2,20),  np.linspace(-2,2,25)
X, Y = np.meshgrid(X, Y)
#Z = (1-X)**2 + 100*(Y-Y**2)**2
Z=exp(-(X**2+Y**2))
ax.plot_surface(X,Y,Z, rstride=1,cstride=1,cmap=cm.jet)
ax.legend()
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')
plt.savefig('surf')
plt.show()