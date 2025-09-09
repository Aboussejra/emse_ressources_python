def moyenne(notes):
    #initialisation des valeurs
    snotes=0
    scoeff= 0
    #Balayage des notes
    for element in notes:
        snotes += element[0]*element[1]
        scoeff += element[1]
    #affichage des valeurs obtenues
    print(snotes, scoeff)
    #calcul de la moyenne
    moy=snotes/scoeff
    #valeur de retour
    return moy

print(moyenne([(15,2),(9,1),(12,3)]))
