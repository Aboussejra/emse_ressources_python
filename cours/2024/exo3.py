def echange(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]

def trichotomie(tab, i, j):
    if tab[i] > tab[j]:
        echange(tab, i, j)
    if (j - i) > 1:
        k = (j - i + 1) // 3
        trichotomie(tab, i, j- k)
        trichotomie(tab, i+k, j)
        trichotomie(tab, i, j-k)
        print("k =",k)

A = [5, 6, 4, 2, 3, 1]
print("avant appel trichotomie:", A)
trichotomie(A, 0, len(A) - 1)
print("apres appel trichotomie:", A)


