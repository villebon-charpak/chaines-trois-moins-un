# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:32:33 2018

@author: etudiant
"""

'''
Maintenant que notre déchifrement avec clé marche on va essayer de déchiffrer un message sans connaitre la clé,
pour cela nous nous sommes réparti les taches,
répartition  des taches : 
Lehui : compter les occurences dans le message et identifier celui qu'est le plus répété en nombre ascii (on saura que c'est l'espace)
Camille : identifier celui qu'est le plus répété en nombre ascii (on saura que c'est l'espace) déterminer la clé
Samuel : demander a l'utilisateur si le message a bien été decripté sinon recommencer (on utilisera alors le 2ème caractère le plus utilisé en tant qu'espace)