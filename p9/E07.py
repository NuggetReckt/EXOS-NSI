prix = 56
reduc1 = 0.04
reduc2 = 0.03

print("Le prix avec la premiere réduction est de :", prix - prix * reduc1, "€")
print("Le prix avec la seconde réduction est de :", prix - prix * reduc2, "€")
print("Le taux d'ensemble est de : ", reduc1*100 + reduc2*100, "%")

print("Le prix final est de :", prix - (prix * reduc1) - (prix * reduc2), "€")
