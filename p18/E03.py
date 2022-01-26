nb = int(input("Rentrez le nombre de mois : "))

S = 1200

for i in range(0, nb):
    S *= 1.0015

print("Somme totale :", round(S))
