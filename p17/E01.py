p = int(input("Rentrez votre poid : "))
t = float(input("Rentrez votre taille : "))

print("Calcul...")

imc = p/(t**2)

print("Votre IMC est de :", round(imc))

if imc < 25:
    print("Tout vas bien")
elif imc <= 30:
    print("Tendance à l'obésité")
elif imc > 30:
    print("Obésité certaine")
