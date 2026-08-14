"""
Du tableau numpy au tableau de donnees pandas.
Un DataFrame est un tableau a colonnes nommees : c'est la structure
que l'on manipule des que les donnees viennent d'un fichier.
"""
import pandas as pd

# ---- 1. construire un DataFrame a partir de listes ----
ages = [54, 61, 47, 33, 68, 29]
imc = [21.5, 24.0, 27.8, 19.9, 31.2, 22.4]
glycemie = [0.95, 1.12, 0.99, 0.97, 1.31, 0.85]

df = pd.DataFrame({"age": ages, "imc": imc, "glycemie": glycemie})
print(df)

# ---- 2. lire un fichier CSV : c'est le cas reel ----
df = pd.read_csv("patients.csv")
print(df.head())

# ---- 3. decrire le jeu de donnees ----
print("dimensions (lignes, colonnes) =", df.shape)
print("valeurs manquantes par colonne :")
print(df.isna().sum())

# ---- 4. statistiques descriptives de toutes les colonnes numeriques ----
print(df[["age", "imc", "glycemie"]].describe())

# ---- 5. selectionner une colonne, filtrer des lignes ----
print("glycemie moyenne =", df["glycemie"].mean())
print("patients au-dessus du seuil de 1.26 g/L :")
print(df[df["glycemie"] > 1.26])

# ---- 6. comparer des sous-groupes ----
print("glycemie moyenne selon le tabagisme :")
print(df.groupby("tabac")["glycemie"].mean())
print("effectifs et moyennes selon le sexe :")
print(df.groupby("sexe")[["age", "imc", "glycemie"]].mean())

# ---- 7. creer une nouvelle colonne ----
df["surpoids"] = df["imc"] >= 25
print("nombre de patients en surpoids =", df["surpoids"].sum())
print(df.groupby("surpoids")["glycemie"].mean())
