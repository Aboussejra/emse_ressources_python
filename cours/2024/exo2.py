import time
import matplotlib.pyplot as plt

def puiss(a,n):
    if n==0:
        return 1
    else:
        r=1
        for k in range(n):
            r=r*a
        return r
    
def puissr(a,n):
    global k
    if n==1:
        return a
    else:
        if n%2==0:
            k=k+1
            return (puissr(a,n/2))**2
        else:
            k=k+1
            return a*(puissr(a,(n-1)/2))**2

print(puiss(1.01,2))

global k
k=0
print(puissr(1.01,100))

li=[]
tr=[]
ts=[]
tk=[]
for l in range(1,10001):
    #indice
    li.append(l)
    #calcul iteratif
    start=time.time()
    puiss(1.01,l)
    stop=time.time()
    ts.append(stop-start)
    #calcul recursif
    k=0
    start=time.time()
    puissr(1.01,l)
    stop=time.time()
    tr.append(stop-start)
    tk.append(k)

plt.figure(0)
plt.clf()
plt.grid(True)
plt.loglog(li,ts,'b-',label='iteratif')    
plt.loglog(li,tr,'r-',label='recursif') 
plt.xlabel(r'$n$') 
plt.ylabel(r'$t(n)  [s]$')   
plt.legend(loc='best')
plt.savefig("exo2-time.png",dpi=400)

plt.figure(10)
plt.clf()
plt.grid(True)
plt.xlabel(r'$n$') 
plt.ylabel(r'$k(n)$')  
plt.loglog(li,tk,'b-')        
plt.savefig("exo2-appel-recursif.png",dpi=400)

