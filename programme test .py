

def compter_occurences(mot, chaine):# définir une fonction qui compte le nombre de 'mot' dans une chaine de caractère
    compteur = 0
    for i in range (len(chaine)-len(mot)+1): #fonction permettant à i de parcourir de 0 à n (si c'est i in range (n)) 
                                            # len permet de donner à chaque lettre dans la chaine de caractère un chiffre correspondant
        if chaine [i:i+len(mot)]==mot: 
            compteur +=1
    return compteur



def decaler (caractere1,decalage):
    caractere = ord(caractere1)
    b = caractere + decalage
    lettre_changee = chr(b)
    return lettre_changee

message1 = 'hfjhjfj'
for i in range (len(message1)):
    a = ord(message1)
    print (a)
    
    
    
b = intput()
message = 'ajhdgsfdfe'
liste =list(message)
for i in range (len(message)) : #(len(message)):
    chiffre=ord(liste[i])
    chiffre += b
    lettre =chr(chiffre)
    print(lettre)