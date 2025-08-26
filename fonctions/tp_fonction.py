
# EXERCICES
# Ecrire un programme qui demande å l'utilisateur de saisir les valeurs de
# deux variables A et B. Ensuite, il permet de définir et d'appeler Ies
# fonctions suivantes :
# Une fonction qui retourne si les valeurs de A et B sont de même signe ou non (Une fonction sans valeur de retour et avec arguments)
# Une fonction qui renvoie le minimum de A et B. (Une fonction avec une  valeur de retour et avec arguments)
# Une fonction qui renvoie le maximum de A et B. (Une fonction avec une valeur de retour et avec arguments)

def signe (a,b):
    if a * b > 0:
        print(f" {a} et {b} sont de meme signe")
    else : 
        print(f" {a} et {b} sont de signe contraire")


def minimum (a, b):
    if a < b :
        return a
    else :
        return b
    
def maximum (a, b):
    if a > b :
        return a
    else :
        return b
    
a = int(input("Entrez la valeur de a :"))
b = int(input("Entrez la valeur de b :"))


# appel de la fonction sans retour avec argument

signe(a, b)

# appel de la fonction avec retour et avec argument

print(f"Le minimum entre {a} et {b} est  : {minimum (a,b)}")
print(f"Le maximum entre {a} et {b} est  : {maximum (a,b)}")


