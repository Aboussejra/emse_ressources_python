#definition de la fonction par recurrence 
def binomrec(k,n):
    if k>n:
       return 0
    elif k==0:
        return 1
    else:
        return binomrec(k-1,n-1)+binomrec(k,n-1)
    
#test 1
k=11
n=10
print("k=",k," n=",n," binom=",binomrec(k,n))

#test 2
k=2
n=5
print("k=",k," n=",n," binom=",binomrec(k,n))
#verification avec la fonction assert
#si la valeur obtenue n'est exacte le message d'erreur
# "erreur de codage est affiche"
assert binomrec(k,n) == 10, "erreur de codage"

#test 3
k=0
n=6
print("k=",k," n=",n," binom=",binomrec(k,n))
