

# condition simple (un choix)
a = int(input("Saisir le premier nombre :"))
b = int(input("Saisir le second nombre :"))

maximum = a

if a < b :
    maximum = b
    
print(f"Maximum est egal à {maximum}")


# verifier si le nombre saisie est positif pu négatif

if a > 0 :
    print(f"{a} est positif")
else :
    print(f"{a} est négatif")
    

# structure conditionnelles multiples


nombre = int(input("Veillez saisir un nombre :"))

if nombre < 0 :
    print(f" {nombre} est négatif")
elif nombre > 0 :
    print(f" {nombre} est positif")
else :
    print(f" {nombre} est null")
    
    
    
