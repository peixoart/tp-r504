def puissance():
    a = input("Choisissez la valeur a : ")
    b = input("Choisissez la valeur b : ")

    if not a.lstrip('-').isdigit():
        raise TypeError("Only integers are allowed for a")
    if not b.lstrip('-').isdigit():
        raise TypeError("Only integers are allowed for b")

    resultat = a ** b
    print(f"Le résultat de {a} à la puissance {b} est égal à {resultat}\n")

puissance()
