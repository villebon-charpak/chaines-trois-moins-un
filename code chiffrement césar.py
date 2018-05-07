# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:09:46 2018

@author: etudiant
"""

# code chiffrement césar :

message = input('message secret : ') #demande un message
cle=input('clé (chiffre entre -26 et 26) : ') #demande la cle



for i in range (len(message)) : #len(message) = longueur du message 
    lettre_cle=ord(message[i]) # on demande la notation ASCII de chaque lettre
    lettre_cle +=int(cle) # on incrémente la clé
    print(chr(lettre_cle)) # on repasse de la notation ascii en lettre
    
#le message s'affiche à la verticale alors qu'il faut qu'il soit a l'horizontale
#attention aux espaces (il faut les laisser)
#apres la lettre z ou avant la lettre a le code marche pas, car ASCII n'est pas une boucle 













