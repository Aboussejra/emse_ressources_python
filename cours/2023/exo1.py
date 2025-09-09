import numpy as np
import matplotlib.pyplot as plt
import time

def rec0(n):
    if n==0:
       return 1
    else:
       return rec0(n-1)**2+1/rec0(n-1)+np.exp(-rec0(n-1))

def rec1(n):
    if n==0:
       return 1
    else:
       rec=rec1(n-1)
       return rec**2+1/rec+np.exp(-rec)

def scal(n):
    x=1
    for i in range(n):
        x=x**2+1/x+np.exp(-x)
    return x

print(rec0(10))
print(rec1(10))
print(scal(10))
ln=[]
d0=[]
d1=[]
ds=[]
for k in range(10):
    ln.append(k)

    tic=time.time()
    rec0(k)
    toc=time.time()
    d0.append(toc-tic)

    tic=time.time()
    rec1(k)
    toc=time.time()
    d1.append(toc-tic)

    tic=time.time()
    scal(k)
    toc=time.time()
    ds.append(toc-tic)

plt.figure(0)
plt.clf()
plt.grid(True)
plt.loglog(ln,d0,'ro-',label='rec 0')
plt.loglog(ln,d1,'bo-',label='rec 1')
plt.loglog(ln,ds,'go-',label='scal')
plt.xlabel(r'$n$')
plt.ylabel(r'$t(n)\quad{}[s]$')
plt.legend(loc='best')
plt.savefig('exo1.png',dpi=400)

