#valeur indice de depart
debut    = 20 

#initialisation du compteur
compteur = debut

#valeur indice de fin
fin      = 71

#Tant que la condition est verifiee on affiche la valeur obtenue
while (compteur < fin):
   compteur = compteur + 1
   if compteur %2==0 and compteur %3==0:
       print(compteur ,"multiple de 2 et 3")
