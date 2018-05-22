# -*- coding: utf-8 -*-

compteur_de_boucle=0
message = input('message secret : ') #demande un message
#cle= tableau_occurence[int(compteur_de_boucle) ]#input('clé (chiffre entre -26 et 26) : ') #demande la cle
def compter_occurences(lettre1, message): # compter le nombre de fois ou apparait la lettre
    compteur = 0
    for lettre in message: 
        if lettre == lettre1:
            compteur += 1
    return compteur 



liste = [] # definit une la liste nommée très judicieusement liste

for i in range (0,127):# pour i allant de a à z en chiffre, chr fait passer de chiffre en lettre
    liste.append(compter_occurences(chr(i),message)) # faire la liste du nombre d'occurence de chaque lettre

tableau_occurence = [] # pour classer les lettres dans l'ordre décroissant en fonction de leur occurance

while liste != [0]*127: # tant que dans la liste il n'y a que des 0, répeter la boucle
    a = liste[0]
    indice = 0
    for i in range (0,len(liste)) : # permet de trouver la lettre le plus repétée
        if a < liste[i] :
            a = liste[i] # nombre de fois ou la lettre est repétée
            indice = i # chiffre ASCII correspondant à la lettre        
    tableau_occurence.append(indice) # apporter cet indice dans une nouvelle liste 
    liste[indice] = 0 # remplacer l'occurence à l'indice i par 0

cle = 32 - tableau_occurence[0] #on trouve le décalage : 32 est le numéro qui correspond à l'espace qu'on soustrait par le numéro du caractère codé qui aparaît le plus. 

tableau=[] # on créé un tableau 

for j in range (len(message)) : #len(message) = longueur du message 
    lettre_cle=ord(message[j]) # on demande la notation ASCII de chaque lettre
    lettre_cle +=int(cle) # on incrémente la clé
    if cle < -32 :                  
        lettre_cle -=int(cle)
        print("pas possible") #lorsqu'on soustrait par 32 le résultat est négatif ce qui ne correspond à aucun caractère dans la table ascii
        lettre_cle=chr(lettre_cle) # on repasse de la notation ascii en lettre
        tableau.append(lettre_cle) # on incrémente la lettre dans le tableau
    else :
        lettre_cle=chr(lettre_cle) # on repasse de la notation ascii en lettre
        tableau.append(lettre_cle) # on incrémente la lettre dans le tableau
    
phrase_modifiée = "".join(tableau) # tous les mots sont regroupés et un espace les sépare
print('voici le message déchiffré : ',phrase_modifiée) # on imprime la phrase décodée 
    
a = 0

while a == 0 :
    a= int(input('le message est-il déchiffré ? (si oui tapez 1, si non tapez 0) :'))
    if a==1:
        print('merci pour votre participation, votre message nous aidera à améliorer notre intelligence artificielle')
    elif a==0:
        print('nous allons recommencer ...')
        tableau=[] # on créé un tableau 
        compteur_de_boucle+=1
        print(compteur_de_boucle)
        for i in range (len(message)) :#len(message) = longueur du message 
            cle= 32 - tableau_occurence[int(compteur_de_boucle) ]
            lettre_cle=ord(message[i]) # on demande la notation ASCII de chaque lettre
            lettre_cle +=int(cle) # on incrémente la clé
            lettre_cle=chr(lettre_cle) # on repasse de la notation ascii en lettre
            tableau.append(lettre_cle) # on incrémente la lettre dans le tableau
    
        phrase_modifiée = "".join(tableau)
        
        
        print('voici le message déchiffré : ',phrase_modifiée)
        
    else :
        print('nous avons affaire à un génie ...')



