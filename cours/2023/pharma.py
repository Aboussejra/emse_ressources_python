from random import *

def pharma(liste):
    n2=len(liste)//2
    l1=[]; l2=[]
    for i in liste:
        if randint(1,2)==1:
           if len(l1)<n2:
              l1.append([i])
           else:
              l2.append([i])
        else:
           if len(l2)<n2:
              l2.append([i])
           else:
              l1.append([i])
    return(l1,l2)

liste=["a","b","c","d","e","f"]
l1,l2=pharma(liste)
print("l1=",l1)
print("l2=",l2)
