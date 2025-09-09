# -*- coding: utf-8 -*-
"""
Manipulations de fichiers
"""
#importation module math pour calcul sinus
import math

#creation du fichier toto.txt en ecriture 
#--> option 'w' i.e write
#MyFile est le nom logique
MyFile=open('toto.txt','w')

#la methode write ecrit le mot toto dans le fichier
#on passe a la ligne avec le symbole \n
# i.e n = newline
MyFile.write('toto\n')

#on calcule le sinus puis on sauvegarde le resultat
MyFile.write(str(math.sin(0.9))+'\n')

#on sauvegarde le reel 2.35
MyFile.write(str(2.35))

#on ferme le fichier
MyFile.close()

#on ouvre le fichier en lecture
#--> option 'r' i.e. read
MyFile=open('toto.txt','r')

#lecture de toutes les lignes et affichage a l'ecran
#on utilise la methode readlines
for l in MyFile.readlines():
    print(l)

#on ferme le fichier
MyFile.close()

#on ouvre le fichier et on concatene a la fin de celui-ci
#---> option 'a' i.e. append
MyFile=open('toto.txt','a+')
#on ajoute a la ligne suivante la chaine on ajoute
MyFile.write('\non ajoute\n')

#on ferme le fichier
MyFile.close()

#on lit le fichier
MyFile=open('toto.txt','r')

#on affiche tout le contenu du fichier
a=MyFile.read()#lecture de tout le fichier
print(a)

#on ferme le fichier
MyFile.close()
