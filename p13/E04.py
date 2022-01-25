x = int(input("Rentrez le nombre x :"))
y = int(input("Rentrez le nombre y :"))

if x >= y:
    print("Les nombres restent inchangés")
elif x < y:
    x, y = y, x
    print("x :", x, " y :", y)
    