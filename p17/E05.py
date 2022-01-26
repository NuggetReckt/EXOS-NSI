nb = int(input("Rentrez un nombre : "))

if nb % 2 != 0 and nb % 3 != 0:
    print("Le nombre n'est pas divisible par 2 et par 3")
elif nb % 2 != 0:
    print("Le nombre n'est pas divisible par 2")
elif nb % 3 != 0:
    print("Le nombre n'est pas divisible par 3")
else:
    print("Le nombre est divisble par 2 et par 3")
