# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:59:24 2018

@author: etudiant
"""
def decaler(caractere, decalage):
    caractere = ord(caractere)
    b = caractere + decalage
    lettre_changee = chr(b)
    return lettre_changee

print(decaler(input('caractere: '),2))
    
    
    