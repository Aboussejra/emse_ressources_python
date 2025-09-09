# -*- coding: utf-8 -*-
"""
"""

def pascal(n):
    c = [[1]]
    for k in range(1, n+1):
        ck = [1]
        for i in range(1, k):
            ck.append(c[k-1][i-1] + c[k-1][i])
        ck.append(1)
        c.append(ck)
    return c

def sauvegarder_pascal(n, nom_fichier):
    c = pascal(n)
    file= open(nom_fichier,'w')
    for ligne in c:
        for j in ligne:
            file.write(str(j)+" ")
        file.write("\n")
    file.close()

print(pascal(4))
sauvegarder_pascal(4,"pascal-4.txt")
