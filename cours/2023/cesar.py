ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def position_alphabet(lettre):
    return ord(lettre) - ord('A')
def cesar(message, decalage):
    resultat = ''
    for c in message:
        d=c.upper()
        if 'A' <= d and d <= 'Z':
            indice = (position_alphabet(d) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + d
    return resultat

print(cesar('PHARMACIEN EXPERT EN PYTHON',7))
print(cesar('WOHYTHJPLU LEWLYA LU WFAOVU',-7))

