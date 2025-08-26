# les fonctions en python

# def nom_fonction( arg1, arg2):
#     insstruction 1
#     Instruction 2
#     return resultat

# definir une fonction qui permet de dire bonjour et bienvenu

# fonction sans arguments sants retour
def salutation ():
    print("Bonjour et bienvenue")


# fonction sans retour avec arguments
def hello (nom, prenom):
    print(f"Bonjour {nom} {prenom}")

# fonction avec argument avec retour

def somme(a, b):
    c= a + b
    return c


# appeler une fonction

#  fonction sans argument sans retour

salutation()

# fonction sans retour avec argument

nom =  input ("Votre nom : ")
prenom =  input ("Votre prenom : ")

hello (nom, prenom)


# fonction avec argument avec retour

x = 10  ;  y=30
print (f"Somme =  {somme(x,y)} ")



def addition (a, b):
    c = a + b 
    print("a + b ", c)

a = int(input("Valeur de a :"))
b = int(input("Valeur de b :"))

addition (a, b)

def soustarction (a, b):
    c = a - b
    return c
