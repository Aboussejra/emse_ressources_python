#valeur indice de depart
debut =20

#valeur indice de fin
fin   =71

#indice de boucle
# mot clef: range : cree une liste dont les indices sont
# debut, debut+1, ...., fin-1
#remarquer l'indentation qui apparait apres le symbole :

#pour tester si un nombre a est un multiple de b, 
#on calcule le reste dans la division euclidienne de a par b  
#par l'instruction a%b
#on verifie qu'il est egal a 0
# exemple 13 = 6*3+1 : 13 pas divisible par 3
#         reste de la division euclidienne de 13 par 3 est egal a 1
#         6  = 2*3+0 :  6 est divisible par 3
# 
# pour tester deux conditions on utilise le mot clef and
for iter in range(debut ,fin):
    if iter %2==0 and iter %3==0:
        print(iter ,"multiple de 2 et 3")