#bibliotheque numpy
import numpy as np

#creation d'un vecteur de taille fixee
#les elements sont de type reels
a=np.array([1.0,2.0,3.0,4.0])

#creation d'un vecteur de taille n
#formule donnee
n=32
#creation d'un vecteur de taille nulle
b=np.zeros(n)
#calcul de chaque element
for i in range(n):
    b[i]=float(i)

#chaque vecteur est un objet auquel sont associees
#diverses methodes    
#calcul de la norme du vecteur
na=np.linalg.norm(a)
print(na)

#creation d'une matrice c
c=np.array([[1,2],[3,4]])

#calcul du determinant de la matrice c
dc=np.linalg.det(c)
print(dc)

#creation d'une matrice d
d=np.array([[1,1],[1,1]])

#somme de deux matrices
e=c+d

#produit de deux matrices
f=np.matmul(c,d)
print(f)



    