a = int(input("Rentrez un nombre : "))
b = int(input("Rentrez un nombre : "))
c = int(input("Rentrez un nombre : "))

if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
    print("Ces nombres peuvent être des longueurs d'un triangle rectangle")
else:
    print("Ces nombres ne peuvent pas être des longueurs d'un triangle rectangle")
