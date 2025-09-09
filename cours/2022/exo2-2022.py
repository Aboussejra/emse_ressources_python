# -*- coding: utf-8 -*-
"""
"""
import matplotlib.pyplot as plt

def fibonacci(n):
    u4=3
    u3=2
    u2=0
    u1=1
    for i in range (4,n+1):
        u5=3*u4+2*u3-4*u2+7*u1  
        u1=u2
        u2=u3
        u3=u4
        u4=u5
    return u4

def fibonaccisuite (n):
    file=open("fibo.txt",'w')
    for i in range(n+1):
        file.write(str(i)+ " "+ str(fibonacci(i))+ "\n")
    file.close()
        
x=[]
y=[]
for i in range(1,11):
    x.append(i)
    y.append(fibonacci(i))
plt.figure(0)
plt.xlabel('$n$')
plt.ylabel('$Fib(n)$')
plt.grid(True)
plt.xlim((0.5,10.5))
plt.yscale('log')
plt.plot(x,y,'ko-')
plt.savefig('fibo.png',dpi=400)

