#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercice 1
"""
import numpy as np
import matplotlib.pyplot as plt
import time

#version scalaire de la formule de viete
def viete(N):
    l=[]
    l.append(np.sqrt(2))
    for k in range(1,N):
        l.append(np.sqrt(2+l[k-1]))
    return 2/(np.prod(np.array(l))/2**(N))

vi=[]
vv=[]
vt=[]
for k in range(1,100):
    deb=time.time()
    g=viete(k)
    fin=time.time()
    vi.append(k)
    vv.append(g)
    vt.append(fin-deb)

plt.figure(0)
plt.clf()
plt.grid(True) 
plt.xlabel(r'$n$')
plt.ylabel(r'$v(n)$')
plt.scatter(vi,vv,c='k')
plt.title("Algorithme de Viete")
plt.savefig('viete-val.png',dpi=400)   

plt.figure(1)
plt.clf()
plt.grid(True) 
plt.xlabel(r'$n$')
plt.ylabel(r'$t(n)\,[s]$')
plt.title("Algorithme de Viete")
plt.loglog(vi,vt,'ko-')
plt.savefig('viete-tim.png',dpi=400)   


#---------------------

# version scalaire de la formule de gregory
def gregs(n):
    s=0
    for k in range(n):
        s+=4*(-1)**k/(2*k+1)
    return s

# version recursive de la formule de gregory
def gregr(n):
    if n==0:
        return 4
    else:
        return 4*(-1)**n/(2*n+1)+gregr(n-1)

gi=[]
gv=[]
gt=[]
for k in range(1,100):
    deb=time.time()
    g=gregr(k)
    fin=time.time()
    gi.append(k)
    gv.append(g)
    gt.append(fin-deb)
    
plt.figure(2)
plt.clf()
plt.grid(True) 
plt.xlabel(r'$n$')
plt.ylabel(r'$g(n)$')
plt.scatter(gi,gv,c='k')
plt.title("Algorithme de gregory recursif")
plt.savefig('greg-val.png',dpi=400)   

plt.figure(3)
plt.clf()
plt.grid(True) 
plt.xlabel(r'$n$')
plt.ylabel(r'$t(n)\,[s]$')
plt.loglog(gi,gt,'ko-')
plt.title("Algorithme de gregory recursif")
plt.savefig('greg-tim.png',dpi=400)   
