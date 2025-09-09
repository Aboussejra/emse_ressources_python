# -*- coding: utf-8 -*-
"""
"""

def verifie(tableau):

  for i in range(1, len(tableau)):
   
    if tableau[i] < tableau[i-1]:
      return False
  
  return True

print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))

