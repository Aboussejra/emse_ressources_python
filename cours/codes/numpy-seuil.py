"""
Vectorisation et masques booleens avec numpy.
On repere les patients dont la glycemie a jeun depasse le seuil de 1.26 g/L.
"""
import numpy as np

glycemies = np.array([0.92, 1.05, 1.31, 0.88, 1.42, 0.97, 1.11, 1.68, 0.85, 1.02])
SEUIL = 1.26

# une operation ecrite sur le tableau s'applique a tous les elements :
# pas besoin de boucle. On convertit g/L en mmol/L (facteur 5.55).
en_mmol = glycemies * 5.55
print("mmol/L =", np.round(en_mmol, 2))

# un test de comparaison renvoie un tableau de booleens : c'est un "masque"
masque = glycemies > SEUIL
print("masque =", masque)

# on selectionne les valeurs correspondantes en indexant par le masque
au_dessus = glycemies[masque]
print("valeurs au-dessus du seuil =", au_dessus)

# somme d'un tableau de booleens = nombre de True
nb = masque.sum()
proportion = nb / glycemies.size
print("effectif au-dessus du seuil =", nb)
print("proportion                  =", proportion)

# indices des patients concernes
print("indices =", np.where(masque)[0])

# centrage-reduction (score z) : combien d'ecarts-types au-dessus de la moyenne
z = (glycemies - glycemies.mean()) / glycemies.std()
print("scores z =", np.round(z, 2))
