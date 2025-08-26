
# Introduction à python
# Les variables en python

# quoi sert une variable
# Une variable permet d'associer un objet un nom. On peut ensuite accder cet objet en mmoire grce au nom de la variable.

# Cela a plusieurs avantages :

# On peut r-utiliser un objet diffrents endroits de notre code plus rapidement.

# On peut modifier un objet un seul endroit et rpercuter ces changements partout dans notre script.

# Des objets et des noms

# Quand on cre une variable, on associe un objet un nom.

# Il est important de comprendre ce concept et de comprendre qu'un mme objet peut ainsi tre associ plusieurs noms diffrents.

# Cela peut parfois nous jouer des tours, notamment avec les objets muables (que l'on peut modifier) comme les listes :

# >>> a = [1, 2, 3]
# >>> b = a
# >>> b += [4]
# >>> print(a)
# [1, 2, 3, 4]
# Dans l'exemple ci-dessus, les noms a et b pointent vers la mme liste en mmoire.

# Ainsi, quand on modifie la liste, on modifie un seul et mme objet. Les variables a et b pointant vers ce mme objet en mmoire, on modifie donc a et b.

# Affectations simples, parallles et multiples
# Il existe trois faons principales d'affecter une valeur une variable :

# L'affectation simple

# L'affectation parallle

# L'affectation multiple

# Avec l'affectation simple, on associe une valeur une variable :

# a = 5

# Avec l'affectation parallle, on associe plusieurs valeurs plusieurs variables :

# a, b = 5, 10

# Avec l'affectation multiple, on associe une valeur plusieurs variables :

# a = b = 5

# Singleton et 'small integer caching'
# Python dispose de nombreux processus interne qui permettent d'optimiser vos scripts. Parmis ces processus, on retrouve le concept de Singleton et de small integer caching.

# Le mot Singleton fait rfrence au fait qu'un objet est unique.

# C'est le cas de plusieurs objets de Python comme les boolens True et False ou l'objet None.

# Quand vous crez un boolen True, vous rfrez ainsi toujours au mme objet en mmoire.

# Ce mme concept est valable pour certains objets comme les nombres compris entre -5 et 256 et les chanes de caractres courtes.

# Rgles et conventions de nommage
# Il existe plusieurs conventions trs suivies dans la communaut Python que vous retrouverez sous le nom de PEP8.

# Parmi ces conventions, on retrouve de nombreuses conventions de nommage qui indique les rgles suivre lorsque l'on cre des noms de variable.

# Ainsi, il est conseill d'utiliser uniquement des lettres en minuscule et des tirets du bas pour sparer les mots.

# Voici quelques exemples de noms de variables qui respectent ces rgles :

# website_url

# number_of_students

# bank_account_id

# name

# Et quelques contre-exemples :

# StudentID

# Lastname

# firstName

# PhoneNUM

# Votre script fonctionnera si vous ne suivez pas ces conventions. Mais elles sont trs respectes dans la communaut Python et permettent d'avoir une uniformit trs agrable parmi les scripts sur lesquels vous allez travailler.

# Si vous respectez toutes ces conventions et que vous vous habituez les utiliser, vous verrez qu'avec en plus la syntaxe pure de Python, il vous sera trs facile de lire des scripts d'autres dveloppeurs.


nom = input("Entrez votre nom: ")
print(type(nom))  # retourne <class 'str'>. La fonction input retourne toujours une chaîne de caractères.

age = input("Entrez votre age :")
# Vous pouvez par la suite convertir la variable nombre en nombre entier grâce à la fonction int
# nombre = int(nombre)
# print(type(nombre))  # retourne <class 'int'>. La variable a bien été convertie.

resultat = f" Bonjour {nom}, vous avez {age} ans."

print(resultat)

print(type(nom))

print(type(age))