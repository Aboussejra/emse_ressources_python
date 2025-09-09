def fibonacci(n):
    #initialisation de la suite
    u1 = 1
    u2 = 1
    #calcul de chaque terme
    for i in range(n-1):
        tmp = u1
        u1 = u2
        u2 += tmp
    return u1

def fibonaccisuite(n):
    #creation du fichier en ecriture
    File=open('fibo.txt','w')
    #ecriture sur le fichier des valeurs
    for i in range(n+1):
        File.write(str(i)+' '+str(fibonacci(i))+'\n')
    #fermeture du fichier
    File.close()

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(25))
print(fibonacci(45))

fibonaccisuite(40)
