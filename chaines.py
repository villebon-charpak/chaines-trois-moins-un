#!/usr/bin/env python
# encoding : utf-8


#################################################################################################
#   _                _         _                  _                           _   __            #
#  | |   ___ ___  __| |_  __ _(_)_ _  ___ ___  __| |___   __ __ _ _ _ __ _ __| |_ \_\ _ _ ___   #
#  | |__/ -_|_-< / _| ' \/ _` | | ' \/ -_|_-< / _` / -_) / _/ _` | '_/ _` / _|  _/ -_) '_/ -_)  #
#  |____\___/__/ \__|_||_\__,_|_|_||_\___/__/ \__,_\___| \__\__,_|_| \__,_\__|\__\___|_| \___|  #
#                                                                                               #
#################################################################################################

# Le but final de cette activité est d'écrire petit programme de cryptographie qui permet de chiffrer et déchiffrer des messages en utilisant le chiffrement de César. On devrait au final arriver notamment à déchiffrer des messages comme ceux-ci :

message_secret1 = 'mhvxlvmxohvfhvdu'
message_secret2 = 'dwwdtxhdodxeh'
message_secret3 = "Mðspjp{h{pvuz'(']v|z'ñ{lz'hyyp}ðz'ç'kðjopmmyly'jl'tlzzhnl5'Sl'jvkl'kl'Jðzhy'u.h'kðzvythpz'ws|z'kl'zljyl{z'wv|y'}v|z5"

# Chemin faisant, nous prendrons aussi l'occasion pour voir (ou revoir) comment on manipule du texte en informatique (et plus particulièrement en Python) !

# En informatique, une chaîne de caractère (string en anglais) est le type qui permet la manipulation du texte par un programme. Une chaîne de caractère est tout simplement une séquence de symboles (lettres, espaces, saut de lignes, caractères de ponctuations, symbôles divers). En somme, du texte brut (sans formattage) comme on en trouverait dans un fichier txt. Passons en revue quelques fonctionnalités de bases des chaines de caractères.

######################
# définir une chaine #
######################
# Pour définir une chaine de caractère dans Python, on peut taper une séquence de symboles délimitée au début et à la fin par des accolades ', des  guillements ", ou des triples guillemets """ :

ma_chaine1 = 'Je ne saute pas '
ma_chaine2 = "de ligne !"
ma_chaine3 = """Un texte mis entre triples guillemets peut contenir des
sauts
de lignes."""

# On peut ne rien mettre entre les symboles d'ouverture et fermeture, on crée alors une chaine vide :

chaine_vide = '' # une chaine de caractère qui ne contient aucun caractère !

#########
# print #
#########
# La fonction print permet d'afficher une chaine de caractère. Notez que la fonction passe à la ligne à chaque appel :

print("Deux appels successifs de la fonction print :")
print(ma_chaine1) # saut de ligne
print(ma_chaine2)

#################
# concaténation #
#################
# Sur les chaines de caractères, on dispose d'un opérateur de concaténation, noté par le symbole +, qui crée une chaîne composée des deux chaines accolées à la suite :

print("Avec concaténation :")
print(ma_chaine1 + ma_chaine2)

################################
# multiplication par un entier #
################################
# On peut multiplier une chaine de caractères par un entier pour la répéter plusieurs fois :

print("All work and no play makes Jack a dull boy.\n" * 10)

#########
# input #
#########
# la fonction input permet de demander à l'utilisateur de saisir une chaine de caractères. Le programme attend alors que l'utilisateur tape du texte au clavier. L'éxecution du programme reprend dès que l'utilisateur appuie sur la touche entrée :

ma_chaine4 = input("Veuillez saisir du texte : ")
print("Tu as tapé : " + ma_chaine4)


#######
# str #
#######
# On peut convertir une variable en une chaine de caractère à l'aide de la fonction str :

quarante_deux = str(42) # '42'

print("la réponse est " + quarante_deux)



print(
"""
######################################
# Parcourir une chaine de caractères #
######################################
"""
)
# On peut manipuler une chaine de caractères de manière assez similaire à un tableau. Par exemple, on peut accéder à une partie d'une chaine de cartères comme pour un tableau à l'aide de la syntaxe chaine[i] :

chaine = "Bonjour !"

print(chaine[0])    # B
print(chaine[:3])   # Bon
print(chaine[3:])   # jour !
print(chaine[4:6])  # ou
print(chaine[-1])   # !

#######
# len #
#######
# Comme pour les tableaux, la fonction len() retourne la longueur d'une chaine.

print(len("chaine de caractères")) # 20

# L'utilisation de la fonction len() permet notamment le parcours d'une chaine de caractère comme une liste. Selon vous, que fait le code de la fonction suivante ?

def fonction(chaine):
    compteur = 1
    for i in range(len(chaine)):
        if chaine[i] == ' ':
            compteur += 1
    return compteur
    
# Vous pouvez tester votre hypothèse en utilisant la fonction sur des exemples :
print("test de la fonction :")
nombre = fonction("ma super chaine")
print(nombre)

# La boucle for peut également parcourir directement les éléments de la chaine, sans utiliser les indices : 

for caractere in chaine :
    # on fait des choses
    pass
    
def fonction(chaine):
    compteur = 1
    for caractere in chaine:
        if caractere == ' ':
            compteur += 1
    return compteur

##### 
# 1 #
#####

# Niveau 1 : À l'aide d'une boucle for, programmer une fonction compter_occurences(caractere, chaine) qui retourne le nombre d'occurence du caractère c dans la chaîne s


def compter_occurences(caractere, chaine):
    # retourne le nombre d'occurences du caractère dans la chaine
    
    pass # remplacer cette ligne par votre code
 
# quelques tests : 
# assert compter_occurences('o', 'bonjour') == 2
# s = "En ce mement, certes, t’es le chef, mets – beleve me – ce temps est bref et je prefere etre dens mes semelles qe dens tes empegnes !"
# assert compter_occurences('e', s) == 35
# assert compter_occurences('a', s) == 0



##### 
# 2 #
#####

# Niveau 1 : En utilisant votre fonction compter_occurence, programmer une fonction compter_mots(chaine) qui retourne le nombre de mot dans la chaine. On suppose ici qu'un mot est simplement une sequence de symbole sans espace (il s'agit d'un modèle très simpliste, mais on s'en contentera). La fonction doit retourner 0 pour une chaine vide.

def compter_mots(chaine):
    # retourne le nombres de mot dans la chaine
    
    pass # remplacer cette ligne par votre code
    
# quelques tests :
# assert compter_mots("") == 0
# assert compter_mots("anticonstitutionnellement") == 1
# assert compter_mots("Ceci est un chaine de caractères qui contient dix mots.") == 10
    
##### 
# 3 #
#####

# Niveau 2 : Toujours à l'aide d'une boucle for programmer une fonction compter_occurences(mot, chaine) qui retourne le nombre d'occurence du mot dans la chaine

def compter_occurences_mot(mot, chaine):
    # retourne le nombre d'occurence de mot dans la chaine
    
    pass # remplacer cette ligne par votre code
    

# quelques tests
# assert compter_occurences_mot('bla', 'blablabla') == 3
# assert compter_occurences_mot('haha', 'hahaha') == 2



#####################################
# Modifier une chaine de caractères #
#####################################

# Contrairement à un tableau, il n'est pas possible de modifier la valeur d'un caractère dans une chaine par affectation (on dit qu'une chaine de caractère est immuable). Par exemple, le code suivant provoque une erreur :

chaine = "adieux canard !"
try :
    chaine[0] = 'o' # va provoquer une TypeError
except TypeError:
    print("Une chaîne de caractères est un objet immuable en Python.")
    
# Pour contourner cette limitation, il peut être utile de transformer une chaine en une liste de caractères à l'aide de la fonction list(). On peut ensuite effectuer l'opération inverse en utilisant ''.join(). Par exemple d'effectuer cette opération (techniquement, on ne modifie pas la chaîne s originale, on la remplace en intégralité par une nouvelle chaîne): 

liste = list(chaine) # on transforme s en list
liste[0] = 'o' # on change le premier élément de la liste
chaine = ''.join(liste) # on retransforme la liste l en une chaîne
print(chaine)

##### 
# 4 #
#####

# Niveau 1 : En utilisant list et join, programmer une fonction substituer() qui retourne une chaine où l'on a mis un certain caractère en position i.

def modifier(chaine, caractere, i):
    # retourne la chaine dans laquelle le caractère en position i a été modifié pour devenir caractere
    
    pass # remplacer cette ligne par votre code

# tests
# assert modifier("balle", "u", 1) == "bulle"
# assert modifier("adieux canard !", "o", 0) == "odieux canard !"

##### 
# 5 #
#####

# Niveau 2 : Programmer une fonction substituer_mot qui remplace toutes les occurences d'un mot par un autre mot. On pourra utiliser les méthodes split et join. Attention : si le mot de remplacement est vide, on veut en fait supprimer les occurences de mot original.
    
def substituer(chaine, mot, remplacement):
    # retourne la chaine où toutes les occurences de mot ont été remplacées par remplacement
    
    pass # remplacer cette ligne par votre code

# quelques tests
# assert substituer("l'homme est un loup pour l'homme", "l'homme", "le loup") == "le loup est un loup pour le loup"
# assert substituer('Interdiction de prononcer le mot tabou qui est désormais tabou !', 'tabou', '') == 'Interdiction de prononcer le mot qui est désormais !' # attention aux éventuels doubles espaces...


##### 
# 6 #
#####

# Optionnel : À partir de votre fonction substituer, implémenter : https://www.xkcd.com/1288/
# c'est-à-dire programmer une fonction xkcd qui prend en argument une chaine et un dictionnaire de substititions à effectuer, et qui retourne la chaine où toutes les substitutions ont été effectuée.


def xkcd(chaine, substitutions):
    # implématation de https://www.xkcd.com/1288/
    # la fonction prend en argument une chaine et un dictionnaire de substititions à effectuer, et retourne la chaine où toutes les substitutions ont été effectuée.
    
    pass # remplacer cette ligne par votre code


##########################
# La table ASCII/Unicode #
##########################
 
# Pour encoder une chaine de caractère dans la mémoire de l'ordinateur, il faut attribuer à chaque caractère un numéro (qui est stocké en binaire dans la mémoire). Le choix est a priori aribtraire (et il a existé plusieurs standards d'encodages différents), mais deux standards sont très répandus et sont utilisé dans Python : ASCII et Unicode. La table ASCII (American Standard Code for Information Interchange), est une des premières tables de ce genre (sa création remonte aux années 60) et la plus universellement utilisée. Mais elle était conçue pour l'anglais et ne contient aucun caractère accentué, ou autres alphabets. La table Unicode est une extension de la table ASCII qui contient tous ces caractères manquant, et est devenu aujourd'hui le standard dominant.

# En python, pour obtenir le numéro d'un caractère, on utilise la fonction ord()

print(ord('a')) # 97

# Et réciproquement, pour obtenir un caractère à partir de son numéro, on utilise la fonction chr()

print(chr(97)) # a

##### 
# 7 #
#####

# Niveau 1 : À partir des fonctions ord et chr, écrire une fonction decaler(caractere, decalage) qui permet de trouver le caractère un certain nombre de rangs plus loin dans la table ASCII/Unicode

def decaler(caractere, decalage):
    # retourne le caractère qui se trouve un certain nombre de rangs plus loin dans la table ASCII/Unicode (le nombre est donne par l'entier decalage)
    
    pass # remplacer cette ligne par votre code

##### 
# 8 #
#####

# Niveau 2 : En utilisant votre fonction decaler, programmer une fonction chiffrement_cesar qui prend en argument un message (chaine de caractère), et une clé (entier), et retourne le message chiffré par le chiffre de César avec le clé.

  
def cesar(message, cle):
    # retourne le message chiffré par le code de César avec la clé
    
    pass # remplacer cette ligne par votre code

# tests
# assert cesar('bonjour', 1) == 'cpokpvs'
# assert cesar('JulesCesar', 3) == 'MxohvFhvdu'
# assert cesar('glevefme', -4) == 'charabia'

# Niveau 2 : En utilisant votre fonction chiffrement_cesar, programmer une fonction dechiffrement_cesar qui effectue l'opération inverse

def dechiffrement_cesar(message_chiffre, cle):
    # retourne le message déchiffré par le code de César avec la clé
    
    pass # remplacer cette ligne par votre code


# tests
# assert dechiffrement_cesar('cpokpvs', 1) == 'bonjour'
# assert dechiffrement_cesar('MxohvFhvdu', 3) == 'JulesCesar'

#####
# 9 #
#####

# Niveau 3 : Comment trouver la clé d'un message chiffré par le code de césar ? Utilisez cette méthode pour déchiffrer les messages contenus dans les variables message_secret1, message_secret2 et message_secret3

