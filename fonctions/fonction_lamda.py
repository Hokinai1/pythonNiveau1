#Fonction normale
def carre(nombre):
    return nombre * nombre

nombre = 10
x = carre(nombre)
print(x)

# Fonction lamda : tout s'écrit sur une meme ligne

carree_lambda = lambda y: y+y #la fonction

print(f"{carree_lambda(nombre)}")
