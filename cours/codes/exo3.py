def recherche(tab, n):
    result = len(tab)
    if len(tab) > 0:
        for i in range (len(tab)):
            if tab[i] == n:
                result = i

        return result
    else:
        return 'liste vide'


liste=[1,4,8,2]
print('liste=',liste,'resu=',recherche(liste,0))
print('liste=',liste,'resu=',recherche(liste,2))

