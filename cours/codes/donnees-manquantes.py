"""
Valeurs manquantes et valeurs aberrantes dans une liste de mesures.
Sur des donnees reelles, une mesure absente ou une erreur de saisie
fausse silencieusement toutes les statistiques : il faut les reperer.
"""
import numpy as np

# np.nan ("not a number") represente une mesure manquante
mesures = np.array([0.92, 1.05, np.nan, 0.88, 1.42, 0.97, 12.5, 1.68, 0.85, np.nan])

print("nombre de valeurs        =", mesures.size)
print("nombre de valeurs manquantes =", np.isnan(mesures).sum())

# attention : la moyenne classique est contaminee par les nan
print("moyenne naive  =", mesures.mean())

# on retire les valeurs manquantes pour la suite
propres = mesures[~np.isnan(mesures)]
print("valeurs exploitables =", propres)
print("moyenne sur valeurs presentes =", propres.mean())

# detection des valeurs aberrantes par l'ecart interquartile (IQR)
q1 = np.percentile(propres, 25)
q3 = np.percentile(propres, 75)
iqr = q3 - q1
bas = q1 - 1.5 * iqr
haut = q3 + 1.5 * iqr
print("Q1 =", q1, " Q3 =", q3, " IQR =", iqr)
print("intervalle plausible = [", round(bas, 3), ",", round(haut, 3), "]")

aberrantes = propres[(propres < bas) | (propres > haut)]
print("valeurs aberrantes =", aberrantes)

# statistiques une fois les aberrations ecartees
valides = propres[(propres >= bas) & (propres <= haut)]
print("moyenne apres nettoyage =", round(valides.mean(), 4))
print("ecart-type apres nettoyage =", round(valides.std(), 4))
