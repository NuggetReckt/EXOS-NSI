nb = int(input("Rentrez un nombre : "))

somme = 0
for k in range(nb):
    somme += k**2

somme = somme+nb**2
print("Nombre : ", somme)
