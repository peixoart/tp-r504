import fonctions as f

while True : 
	a = int(input("Choisissez la valeur a : "))
        b = int(input("Choisissez la valeur b : "))
	nombre = int(input("Veuillez écrire une valeur : "))
	resultat = f.puissance(a,b)
	print(f"Le carré de {nombre} est {resultat}\n")

