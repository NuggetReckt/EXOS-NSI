nb = int(input("Rentrez un nombre :"))

if nb % 5 == 0 and nb % 3 == 0:
    print("Le nombre est divisible par 3 et 5")
elif nb % 3 == 0:
    print("Le nombre est divisible par 3")
elif nb % 5 == 0:
    print("Le nombre est divisible par 5")
else:
    print("Le nombre n'est divisible ni par 3, ni par 5")
