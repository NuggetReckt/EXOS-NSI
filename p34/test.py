nb = int(input("Rentrez un nombre : "))
maliste = []
for i in range(1, nb+1):
  maliste.append(i)

nbf = 0
for j in maliste:
  nbf += j

print(nbf)
