import math

def quad(a,b,c):
    delta=b*b-4*a*c
    resu=open("quad.txt","a+")
    if delta < 0:
       n=0
       resu.write(str(n)+"\n")
       resu.close()
       return n
    elif delta==0:
       n=1
       r=-b/(2*a)
       resu.write(str(n)+" "+str(r)+"\n")
       resu.close()
       return 1,r
    else:
       n=2
       r1=(-b-math.sqrt(delta))/(2*a)
       r2=(-b+math.sqrt(delta))/(2*a)
       resu.write(str(n)+" "+str(r1)+" "+str(r2)+"\n")
       resu.close()
       return 2,r1,r2

print(quad(1,1,1))
print(quad(1,2,1))
print(quad(1,-5,6))

