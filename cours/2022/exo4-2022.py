# -*- coding: utf-8 -*-
"""
"""
import numpy as np

def moyenne(notes):
    somme=0
    for n in notes:
        somme += n
    moyenne=somme/len(notes)
    
    return moyenne

def ecart_type(notes):
    mean=moyenne(notes)
    som=0
    for i in notes:
        som += (i-mean)**2
    ecart=np.sqrt(som/len(notes))
    
    return ecart

notes=[1,2,3]
print("notes     =",notes)
print("moyenne   =",moyenne(notes))
print("ecart type=",ecart_type(notes))

