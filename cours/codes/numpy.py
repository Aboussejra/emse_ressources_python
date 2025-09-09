#importation module
import numpy as np #alias

#creation tableau 1d d'entiers a la main
x=np.array([1,2,3])
print("x=",x)

#creation tableau 1d de reels a la main
#c'est le point decimal qui permet de definir un reel
y=np.array([1.0,2.0,3.0])
print("y=",y)

#somme de deux tableaux
#conversion automatique de type: entier en reel
z=x+y
print(z)

#nombre d'elements ? 
print("nb elements=",len(z))

#structure du tableau ? 
print(np.shape(z))
#premiere dimension=3
#seconde  dimension= vide
#c'est donc un tableau 1d

#z est un objet
#plusieurs methodes sont accessibles
#type de l'objet: float64
print("type =",z.dtype)
#forme du tableau: 1D seulement
print("shape=",z.shape)
#dimension du tableau: 1D
print("dim  =",z.ndim)

#operation sur le tableau
#v=sqrt(z): operation vectorisee
#aucune boucle n'est requise. 
#Chaque element du tableau est modifie. C'est tres rapide!
v=np.sqrt(z)

#creation d'un tableau rempli de zeros
tab=np.zeros(4)
print(tab)

#creation d'un tableau rempli de un
tab=np.ones(4)
print(tab)

#creation d'un tableau de taille n
#intercale entre a et b n nombres
#c'est une suite arithmetique de raison (b-a)/(n-1)
#attention: l'indice part de 0 a n-1
tab=np.linspace(0,1,4)
print("linspace",tab)

#creation d'un tableau de nombres aleatoires
#un appel a la fonction random de la bibliotheque random de np
tab=np.random.random(4)
print("rand array",tab)
