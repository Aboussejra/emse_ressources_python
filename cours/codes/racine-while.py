#importation du module math
import math

#critere de convergence
err=1.0e-6

#racine
a=2.0

#terme courant
x=a

#nb iterations
iter =0

#solution exacte 
Exact=math.sqrt(a) 

#erreur 1ere iteration
diff=abs(Exact -x) 

#affichage methode choisie
print("Recherche racine carree de 2 par methode Heron")
print("methode : clause while\n")
#Tant que l'erreur obtenue est superieure a la consigne
while diff > err:
    #incrementation compteur
    iter=iter+1 
    #calcul de la valeur approchee par methode d'Heron
    y=0.5*(x+a/x) 
    #calcul de l'erreur
    diff=abs(Exact -y) 
    #echange des valeur x et y pour preparer la nouvelle iteration
    #cela evite de sauvegarder dans une liste toutes les valeurs
    x=y
    #afficher les resultats obtenus 
    print("iter=",iter," err=",diff," val=",x)
    