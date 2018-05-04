# -*- coding: utf-8 -*-
"""
Created on Fri May  4 14:20:38 2018

@author: etudiant
"""

#Question 4 



#chaine [0] = 'o' 
"""
on voit qu'une chaîne de caractère ne peut pas être modifiée, une erreur est affichée.
Pour remplacer un caractère il faut d'abord transfoermer la chaine en liste grâee à la fonction list()
"""
position = int(input("position"))
chaine_initiale = "adieux canard !"
def substituer(chaine_initiale,position,charactere) :

    
    liste = list(chaine_initiale)
    liste[position] = charactere  #on remplace le  caractère par o
    chaine_initiale=''.join(liste) #on retransfortme la liste l en une chaîne
    return chaine_initiale

print(substituer(chaine_initiale,position,input('charactere')))
    
    
    
