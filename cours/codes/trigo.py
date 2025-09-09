import numpy as np
import matplotlib.pyplot as plt

x =np.linspace(0,2*np.pi,100)
c =np.cos(x)
s =np.sin(x)
cs=c+s

plt.figure(0)
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim((0,2*np.pi))
plt.plot(x,c,'r-',label='$cos(x)$')
plt.plot(x,s,'b-',label='$sin(x)$')
plt.plot(x,cs,'g-',label='$cos(x)+sin(x)$')
plt.legend(loc='best')
plt.savefig("trigo.png",dpi=400)


