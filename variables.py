
# Introduction à python
# Les variables en python


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