"""
Statistiques descriptives d'une liste de mesures.
Exemple : glycemies a jeun (g/L) relevees chez 10 patients.
On calcule d'abord "a la main" avec math, puis avec numpy.
"""
import math
import numpy as np

glycemies = [0.92, 1.05, 1.31, 0.88, 1.42, 0.97, 1.11, 1.68, 0.85, 1.02]

# ---- version "a la main" : boucles + module math ----
n = len(glycemies)

somme = 0.0
for x in glycemies:
    somme = somme + x
moyenne = somme / n

somme_carres = 0.0
for x in glycemies:
    somme_carres = somme_carres + (x - moyenne) ** 2
ecart_type = math.sqrt(somme_carres / n)

mini = glycemies[0]
maxi = glycemies[0]
for x in glycemies:
    if x < mini:
        mini = x
    if x > maxi:
        maxi = x

print("--- version math ---")
print("effectif   =", n)
print("moyenne    =", moyenne)
print("ecart-type =", ecart_type)
print("min        =", mini)
print("max        =", maxi)

# ---- version numpy : le meme calcul en une ligne chacun ----
g = np.array(glycemies)

print("--- version numpy ---")
print("effectif   =", g.size)
print("moyenne    =", g.mean())
print("ecart-type =", g.std())
print("min        =", g.min())
print("max        =", g.max())
print("mediane    =", np.median(g))

# ---- on verifie que les deux approches donnent le meme resultat ----
assert abs(moyenne - g.mean()) < 1e-12
assert abs(ecart_type - g.std()) < 1e-12
print("les deux methodes concordent")
