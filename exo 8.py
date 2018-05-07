# -*- coding: utf-8 -*-
"""
Created on Fri May  4 17:00:43 2018

@author: etudiant
"""

#a= input('écrire un message : ')
#list(a)
#print(a)

"""
chaine_initiale = "adieux canard !"
def substituer(chaine_initiale,position,charactere) :
    position = int(input("position"))
    liste = list(chaine_initiale)
    liste[position] = charactere  #on remplace le  caractère par o
    chaine_initiale=''.join(liste) #on retransfortme la liste l en une chaîne
    return chaine_initiale

print(substituer(chaine_initiale,position,input('charactere')))
"""

message = 'ajhdgsfdfe'
liste =list(message)
#liste="".join(liste)
for i in range (len(message)) : #(len(message)):
    a=ord(liste[i])
    a +=1
    print(a)
    
#print(ord(liste[1]))
#print(liste)


'''def chiffrement_cesar(message,cle):
    cle = int(input('clé: '))
    l=message
    '''