
def exo2(l1,l2):
    print('l1 =',l1)
    print('l2 =',l2)
    n=min(len(l1),len(l2))
    print(n)
    l=[]
    for i in range(n):
      l.append(l1[i])
      l.append(l2[i])
    mine=min(l)
    maxe=max(l)
    moye=sum(l)/len(l)
    print('min=',mine)
    print('max=',maxe) 
    print('moy=',moye)
    print('lis=',l)

l1=[0, 1, 2, 7] 
l2=[4, 9]
exo2(l1,l2)
