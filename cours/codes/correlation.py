"""
Lien entre deux series de mesures : indice de masse corporelle (IMC)
et glycemie a jeun, chez 12 patients.
On calcule le coefficient de correlation puis on trace le nuage de points.
"""
import numpy as np
import matplotlib.pyplot as plt

imc = np.array([21.5, 24.0, 27.8, 19.9, 31.2, 22.4,
                26.1, 34.5, 20.3, 23.7, 29.0, 25.2])
glycemie = np.array([0.95, 1.12, 0.99, 0.97, 1.31, 0.85,
                     1.22, 1.40, 1.08, 0.91, 1.02, 1.26])

print("moyenne IMC      =", round(imc.mean(), 2))
print("moyenne glycemie =", round(glycemie.mean(), 3))

# matrice de correlation : le coefficient cherche est hors diagonale
R = np.corrcoef(imc, glycemie)
r = R[0, 1]
print("coefficient de correlation r =", round(r, 4))
print("r au carre                   =", round(r ** 2, 4))

# droite d'ajustement par moindres carres : y = a*x + b
a, b = np.polyfit(imc, glycemie, 1)
print("pente a      =", round(a, 5))
print("ordonnee b   =", round(b, 5))

# trace du nuage de points et de la droite
plt.figure()
plt.plot(imc, glycemie, 'o', color='blue', label='patients')
x = np.linspace(imc.min(), imc.max(), 100)
plt.plot(x, a * x + b, '-', color='red', label='ajustement lineaire')
plt.xlabel("IMC (kg/m2)")
plt.ylabel("Glycemie a jeun (g/L)")
plt.title("Glycemie en fonction de l'IMC (r = " + str(round(r, 3)) + ")")
plt.legend()
plt.grid(True)
plt.savefig("correlation.png", dpi=150, bbox_inches='tight')
plt.show()

# Attention : un coefficient de correlation eleve ne demontre pas
# un lien de cause a effet. Il peut exister un facteur commun
# (ici l'age, par exemple) qui explique les deux mesures a la fois.
