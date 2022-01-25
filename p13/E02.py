nb = input("Rentrez un nombre :")

try:
    int(nb)
    entier = 0
except ValueError:
    entier = 1

if entier == 0:
    print("Le nombre est un entier")
else:
    print("Le nombre n'est pas un entier")