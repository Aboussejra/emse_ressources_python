#definition de la fonction equation
# arguments d'entree
# a
# b
# objectif :
# resolution de l'equation ax+b=0 
def equation(a,b):
    if a==0:
       if b==0:
          print("Infinit\'e de solutions")
       else:
          print("Pas de solution")
    else:
       x=-b/a
       print("a=",a)
       print("b=",b)
       print("x=",x)
    
# resolution de plusieurs equations    
equation(0,1)
equation(0,0)
equation(1,-5)
