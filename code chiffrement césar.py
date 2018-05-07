# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:09:46 2018

@author: etudiant
"""

# code chiffrement césar :

message = input('message secret : ') #demande un message
cle=input('clé (chiffre entre -26 et 26) : ') #demande la cle

tableau=[] # on créé un tableau 

for i in range (len(message)) : #len(message) = longueur du message 
    lettre_cle=ord(message[i]) # on demande la notation ASCII de chaque lettre
    lettre_cle +=int(cle) # on incrémente la clé
    lettre_cle=chr(lettre_cle) # on repasse de la notation ascii en lettre
    tableau.append(lettre_cle) # on incrémente la lettre dans le tableau
    
phrase_modifiée = "".join(tableau)
print('voici le message déchiffré : ',phrase_modifiée)
    
#le message s'affiche à la verticale alors qu'il faut qu'il soit a l'horizontale
#attention aux espaces (il faut les laisser)
#apres la lettre z ou avant la lettre a le code marche pas, car ASCII n'est pas une boucle 

a= int(input('le message est-il déchifré ? (si oui tapez 1, si non tapez 0) :'))
if a==1:
    print('merci pour votre participation, votre message nous aidera a améliorer notre intelligence artificielle')
elif a==0:
    print('nous allons recommencer ...')
else :
    print('nous avons affaire a un génie ...')








