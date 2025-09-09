#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exo4.py
"""
import numpy as np

def partage(l):
    n=len(l)
    print(n)
    if n==0:
        print("liste vide")
        return
    else:
        if n%4!= 0:
            print("liste n ayant pas la bonne taille")
            return
        else:
            #decoupage des listes
            l1=l[int(0*n/4):int(1*n/4)]
            l2=l[int(1*n/4):int(2*n/4)]
            l3=l[int(2*n/4):int(3*n/4)]
            l4=l[int(3*n/4):int(4*n/4)]  
            #calcul des quantites demandees
            v1=np.sum(l1)
            v2=np.prod(l2)
            v3=np.sum(np.sqrt(np.abs(l3)))
            v4=np.sqrt(np.sum(np.square(l4)))
            return l1,l2,l3,l4,v1,v2,v3,v4

#liste n'ayant pas 4*n elements
l=[k for k in range(17)]
partage(l)

#liste vide
partage([])

#liste ayant 4 * n elements    
l=[k for k in range(16)]
l1,l2,l3,l4,v1,v2,v3,v4=partage(l)

