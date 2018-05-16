
message = input('message secret : ') # entrer le message 

def compter_occurences(lettre1, message): # compter le nombre de fois ou apparait la lettre
    compteur = 0
    for lettre in message: 
        if lettre == lettre1:
            compteur += 1
    return compteur

liste = [] # definir une variable contenant la liste

for i in range (97,123): # pour i allant de a à z
    liste.append(compter_occurences(chr(i),message)) # faire la liste du nombre d'occurence de chaque lettre
    
a = 0

for i in range (1,len(liste)) :
    if liste[a] < liste[i] :
        a = i

b = chr(a+87)

print (b)

