total = 0

for i in range(20, 31):
    total = i

if total in range(20, 30):
    gars = round(total * 0.75)
    filles = round(total * 0.25)
    print("Il y a ", gars, "garçons et ", filles, "filles")
else:
    print(".")
