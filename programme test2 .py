
message = input('message secret : ') # entrer le message 

def compter_occurences(lettre1, message): # compter le nombre de fois ou apparait la lettre
    compteur = 0
    for lettre in message: 
        if lettre == lettre1:
            compteur += 1
    return compteur



liste = [] # definir une variable contenant la liste

for i in range (0,127): # pour i allant de a à z en chiffre, chr fait passer de chiffre en lettre
    liste.append(compter_occurences(chr(i),message)) # faire la liste du nombre d'occurence de chaque lettre

tableau_occurence = [] 

while liste != [0]*127: # tant que dans la liste il n'y a que des 0, répeter la boucle
    a = liste[0]
    indice = 0
    for i in range (0,len(liste)) : # permet de trouver la lettre le plus repétée
        if a < liste[i] :
            a = liste[i] # nombre de fois ou la lettre est repétée
            indice = i # chiffre correspondant à la lettre        
    tableau_occurence.append(indice) # apporter cet indice dans une nouvelle liste 
    liste[indice] = 0 # remplacer l'occurence à l'indice i par 0

print(tableau_occurence)


        









