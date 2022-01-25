annee = int(input("Rentrez une année : "))

if annee % 400 == 0:
    print("Lannée est bissextile")
elif annee % 100 == 0:
    print("Lannée n'est pas bissextile")
elif annee % 4 == 0:
    print("Lannée est bissextile")
