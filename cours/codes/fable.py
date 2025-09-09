# -*- coding:Utf-8 -*-

MyFile=open('fontaine.txt','w')

MyFile.write("L'aigle, Reine des airs, avec Margot la Pie,\n")
MyFile.write("Differentes d'humeur, de langage et d'esprit,\n")
MyFile.write("Et d'habit,\n")
MyFile.write("Traversaient un bout de prairie.\n")
MyFile.write(str(1668)+'\n')
MyFile.close()

MyFile=open('fontaine.txt','r')
for l in MyFile.readlines():
    print(l)
