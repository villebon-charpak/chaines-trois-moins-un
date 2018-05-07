# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:01:51 2018

@author: etudiant
"""

"""
Created on Mon May  7 15:01:51 2018

@author: etudiant
"""

message = 'ajhdgsfdfe'#on impose un message
liste =list(message) #on transforme notre message en liste

word=[]

for i in range (len(message)) : #sur toute la longueur du message la fonction fera l'action suivante:
    a=ord(liste[i]) # donne le chiffre ascii
    a= a + 1 #on décale d'une lettre le message (clé = 1 ici) 
    b=chr(a)
    word.append(b)
   
    
#nw=str(word)
phrase_modifiée = "".join(word)
print(phrase_modifiée)






