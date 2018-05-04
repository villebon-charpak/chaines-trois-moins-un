# -*- coding: utf-8 -*-
"""
Created on Fri May  4 14:20:38 2018

@author: etudiant
"""

#Question 4 



#chaine [0] = 'o' 
"""
on voit qu'une chaîne de caractère ne peut pas être modifiée, une erreur est affichée.
Pour remplacer un caractère il faut d'abord transfoermer la chaine en liste grâce à la fonction list()
"""
position = int(input("position")) #on demande à l'utilisateur de choisir la lettre qu'il veut remplacer, le int permet de mettre le input en chiffre
chaine_initiale = "adieux canard !" #le texte à modifier est celui-ci 
def substituer(chaine_initiale,position,charactere) : #on définit une fonction qui va remplacer dans la chaine_initiale (argument 1) à la position donnée (argument 2 ) par un charactère ue l'utilisatur donnera(argument 3)

    
    liste = list(chaine_initiale) #on transforme notre chaine de caractère en liste de manière à pouvoir changer un caractère
    liste[position] = charactere  #on remplace le  caractère à la position choisie par l'utilisateur par un charactère choisi 
    chaine_initiale=''.join(liste) #on retransfortme la liste l en une chaîne
    return chaine_initiale 

print(substituer(chaine_initiale,position,input('charactere'))) # on imprime la nouvelle chaine de caractère
    
    
    
