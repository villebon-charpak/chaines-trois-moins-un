# Les chaînes de caractères

Le but de cette activité est d'écrire petit programme de cryptographie qui permet de chiffrer et déchiffrer des messages en utilisant le chiffrement de César. On devrait arriver notamment à déchiffrer des messages comme ceux-ci :

```python
message_secret1 = 'mhvxlvmxohvfhvdu'
message_secret2 = 'dwwdtxhdodxeh'
message_secret3 = "Mðspjp{h{pvuz'(']v|z'ñ{lz'hyyp}ðz'ç'kðjopmmyly'jl'tlzzhnl5'Sl'jvkl'kl'Jðzhy'u.h'kðzvythpz'ws|z'kl'zljyl{z'wv|y'}v|z5"
```

Chemin faisant, nous prendrons aussi l'occasion pour voir (ou revoir) comment on manipule du texte en informatique (et plus particulièrement en python) !

En informatique, une chaîne de caractères (*string* en anglais) est le type qui permet la manipulation du texte par un programme. Une chaîne de caractères est tout simplement une séquence de symboles (lettres, espaces, saut de lignes, caractères de ponctuations, symboles divers). En somme, du texte brut (sans formatage) comme on en trouverait dans un fichier txt. Passons en revue quelques fonctionnalités de base des chaînes de caractères. Pour une liste bien plus complète, on renvoie à de la documentation en ligne comme le site officiel de python : [https://docs.python.org/fr/3/library/stdtypes.html#text-sequence-type-str](https://docs.python.org/fr/3/library/stdtypes.html#text-sequence-type-str).

Tous les exemples suivants sont contenus dans le fichier chaines.py du repository contenant ce README. **Clonez le repository et vous pourrez effectuer vos tests dans ce fichier, et répondre aux questions du TD**.


## Définir une chaîne

Pour définir une chaîne de caractères dans python, on peut taper une séquence de symboles délimitée au début et à la fin par des guillemets simples ', des  guillements ", ou des triples guillemets """ :

```python
ma_chaine1 = 'Je ne saute pas '
ma_chaine2 = "de ligne !"
ma_chaine3 = """Un texte mis entre triples guillemets peut contenir des
sauts
de lignes."""
``

On peut ne rien mettre entre les symboles d'ouverture et fermeture, on crée alors une chaîne vide :

```chaine_vide = '' # une chaîne de caractères qui ne contient aucun caractère !
```


### `print`

La fonction `print` permet d'afficher une chaîne de caractères. Notez que la fonction passe à la ligne à chaque appel :

```python
print("Deux appels successifs de la fonction print :")
print(ma_chaine1) # saut de ligne
print(ma_chaine2)
```


### Concaténation

Sur les chaînes de caractères, on dispose d'un opérateur de concaténation, noté par le symbole `+`, qui crée une chaîne composée des deux chaînes accolées à la suite :

```python
print("Avec concaténation :")
print(ma_chaine1 + ma_chaine2)
```

### Multiplication par un entier

On peut multiplier une chaîne de caractères par un entier pour la répéter plusieurs fois :

```print("All work and no play makes Jack a dull boy.\n" * 10)
```

### `input`

la fonction `input` permet de demander à l'utilisateur de saisir une chaîne de caractères. Le programme attend alors que l'utilisateur tape du texte au clavier. L'éxecution du programme reprend dès que l'utilisateur appuie sur la touche entrée :

```ma_chaine4 = input("Veuillez saisir du texte : ")
print("Tu as tapé : " + ma_chaine4)
```


### `str`

On peut convertir une variable en une chaîne de caractères à l'aide de la fonction `str` :

```python
quarante_deux = str(42) # '42'
print("la réponse est " + quarante_deux)
```


## Parcourir une chaîne de caractères

On peut manipuler une chaîne de caractères de manière assez similaire à un tableau. Par exemple, on peut accéder à une partie d'une chaîne de cartères comme pour un tableau à l'aide de la syntaxe `chaine[i]` :

```python
chaine = "Bonjour !"
print(chaine[0])    # B      (caractère numéro 0)
print(chaine[:3])   # Bon    (caractères numéro 0, 1 et 2)
print(chaine[3:])   # jour ! (caractères numéros 3 et plus)
print(chaine[4:6])  # ou     (caractères 4 et 5)
print(chaine[-1])   # !      (dernier caratère)
```


### `len`


Comme pour les tableaux, la fonction `len` retourne la longueur d'une chaîne.

```python
print(len("chaine de caractères")) # 20
```

L'utilisation de la fonction `len` permet notamment le parcours d'une chaîne de caractères comme une liste. Selon vous, que fait le code de la fonction suivante ?


```python
def fonction(chaine):
    compteur = 1
    for i in range(len(chaine)):
        if chaine[i] == ' ':
            compteur += 1
    return compteur
```


La boucle `for` peut également parcourir directement les éléments de la chaîne, sans utiliser les indices : 

```python
for caractere in chaine :
    # on fait des choses
    pass
    
def fonction(chaine):
    compteur = 1
    for caractere in chaine:
        if caractere == ' ':
            compteur += 1
    return compteur
```

### Question 1

*Niveau 1 :* À l'aide d'une boucle `for`, programmer une fonction `compter_occurences(caractere, chaine)` qui retourne le nombre d'occurence du caractère `caractere` dans la chaîne `chaine`

### Question 2

*Niveau 1 :* En utilisant votre fonction `compter_occurence`, programmer une fonction `compter_mots(chaine)` qui retourne le nombre de mot dans `chaine`. On suppose ici qu'un mot est simplement une sequence de symbole sans espace (il s'agit d'un modèle très simpliste, mais on s'en contentera). La fonction doit retourner `0` pour une chaîne vide.
    
### Question 3

<<<<<<< Updated upstream
*Niveau 2 :* Toujours à l'aide d'une boucle `for`, programmer une fonction `compter_occurences(mot, chaine)` qui retourne le nombre d'occurence de la chaîne `mot` à l'intérieur de la chaîne `chaine`.
=======
*Niveau 2 :* Toujours à l'aide d'une boucle `for`, programmer une fonction `compter_occurences_mot(mot, chaine)` qui retourne le nombre d'occurence de la chaine `mot` à l'intérieur de la chaîne `chaine`.
>>>>>>> Stashed changes


## Modifier une chaîne de caractères

Contrairement à un tableau, il n'est pas possible de modifier la valeur d'un caractère dans une chaîne par affectation (on dit qu'une chaîne de caractères est **immuable**). Par exemple, le code suivant provoque une erreur :

```python
chaine = "adieux canard !"
try :
    chaine[0] = 'o' # va provoquer une TypeError
except TypeError:
    print("Une chaîne de caractères est un objet immuable en python.")
```
    
Pour contourner cette limitation, il peut être utile de transformer une chaîne en une liste de caractères à l'aide de la fonction `list`. On peut ensuite effectuer l'opération inverse en utilisant `''.join()`. Par exemple d'effectuer cette opération (techniquement, on ne modifie pas la chaîne s originale, on la remplace en intégralité par une nouvelle chaîne) : 


```python
liste = list(chaine) # on transforme s en list
liste[0] = 'o' # on change le premier élément de la liste
chaine = ''.join(liste) # on retransforme la liste l en une chaîne
print(chaine)
```


### Question 4

*Niveau 1 :* En utilisant list et join, programmer une fonction `substituer()` qui retourne une chaîne où l'on a mis un certain caractère en position `i`.


### Question 5

*Niveau 2 :* Programmer une fonction `substituer_mot` qui remplace toutes les occurences d'un mot par un autre mot. On pourra utiliser les méthodes `split` et `join`. Attention : si le mot de remplacement est vide, on veut en fait supprimer les occurences du mot original.


### Question 6

*Optionnel :* À partir de votre fonction substituer, implémenter [https://www.xkcd.com/1288/](https://www.xkcd.com/1288/), c'est-à-dire programmer une fonction `xkcd` qui prend en argument une chaîne et un dictionnaire de substititions à effectuer, et qui retourne la chaîne où toutes les substitutions ont été effectuées.


## La table ASCII/Unicode
 
Pour encoder une chaîne de caractères dans la mémoire de l'ordinateur, il faut attribuer à chaque caractère un numéro (qui est stocké en binaire dans la mémoire). Le choix est a priori aribtraire (et il a existé plusieurs standards d'encodages différents), mais deux standards sont très répandus et sont utilisés dans python : ASCII et Unicode. La table ASCII (American Standard Code for Information Interchange), est une des premières tables de ce genre (sa création remonte aux années 60) et la plus universellement utilisée. Mais elle était conçue pour l'anglais et ne contient aucun caractère accentué, ou autres alphabets. La table Unicode est une extension de la table ASCII qui contient tous ces caractères manquants, et est devenue aujourd'hui le standard dominant.

En python, pour obtenir le numéro d'un caractère, on utilise la fonction `ord` :

```python
print(ord('a')) # 97
```

Et réciproquement, pour obtenir un caractère à partir de son numéro, on utilise la fonction `chr` :

```python
print(chr(97)) # a
```


### Question 7

*Niveau 1 :* À partir des fonctions `ord` et `chr`, écrire une fonction `decaler(caractere, decalage)` qui permet de trouver le caractère un certain nombre de rangs plus loin dans la table ASCII/Unicode.

## Le chiffre de César

En cryptographie, le chiffrement par décalage, aussi connu comme le **chiffre de César**, est une méthode de chiffrement qui fut utilisée par Jules César dans ses correspondances secrètes. Le texte chiffré s'obtient simplement en remplaçant chaque lettre du texte en clair par une lettre à distance fixe, toujours du même côté, dans l'ordre de l'alphabet. Par exemple avec un décalage de 3 vers la droite, A est remplacé par D, B devient E, et ainsi de suite. Ainsi, pour un décalage de 3, le message `'comunicationsecrete'` devient `'frpxqlfdwlrqvhfuhwh'`.

Dans notre implémentation, on effectuera le décalage sur l'ensemble de la table de caractères Unicode, et pas juste les lettres. Cela nous permet de ne laisser aucun symbole en clair. La table est suffisamment grande pour qu'on ne se posera pas le problème de ce qu'il se passe pour les caractères à la fin de la table. À titre d'exemple, pour un décalage de 3, le message `'un message avec des espaces'` devient `'xq#phvvdjh#dyhf#ghv#hvsdfhv'`.

### Question 8

*Niveau 2 :* En utilisant votre fonction `decaler`, programmer une fonction `chiffrement_cesar` qui prend en argument un message (chaîne de caractères), et une clé (nombre entier correspondant au décalage), et retourne le message chiffré par le chiffre de César avec le clé.

*Niveau 2 :* En utilisant votre fonction `chiffrement_cesar`, programmer une fonction `dechiffrement_cesar` qui effectue l'opération inverse.


### Question 9

*Niveau 3 :* Comment trouver la clé d'un message chiffré par le code de César ? Utilisez cette méthode pour déchiffrer les messages contenus dans les variables `message_secret1`, `message_secret2` et `message_secret3`.

