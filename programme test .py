

#Q2
s='gjfhkf'

def compter_mot(chaine): #compter le nombre d'espaces pour déduire le nombre de mots
    if len(chaine)==0: #si il n'a rien dans la chaine de caractère retourner 0 
        return 0
    else :
        compteur = 1 
        for caractere in chaine:
            if caractere == ' ': # pour chaque espace donner +1
                compteur += 1
        return compteur # attention ce programme ne marche pas pour les cas où il y a une espaces tout devant ou tout derrière

print(compter_mot(s))

#Q3
    
a = 'motmotutomzigmotmmmdazmot'


def compter_occurences(mot, chaine):
    compteur = 0
    for c in chaine:
        if c =='m':
            compteur +=0
        if c =='o':
            compteur +=0
        if c=='t':
            compteur +=1
    return compteur

print(compter_occurences('mot',a))
