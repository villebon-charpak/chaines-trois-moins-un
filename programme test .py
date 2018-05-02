# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:53:11 2018

@author: etudiant
"""
# test Q1 :

s = "En ce mement, certes, t’es le chef, mets – beleve me – ce temps est bref et je prefere etre dens mes semelles qe dens tes empegnes !"

message_secret1 = ''

def compter_occurences(lettre, message):
    compteur = 0
    for c in message:
        if c == lettre:
            compteur += 1
    return compteur


def compter_mots(chaine):
    nombreEspaces = compter_occurences(' ',chaine)
    return nombreEspaces + 1

print(compter_mots(message_secret1))
