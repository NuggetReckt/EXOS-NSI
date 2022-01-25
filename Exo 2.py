class CompteBancaire:

    def __init__(self, titulaire, solde=0):
      self.titulaire = titulaire
      self.solde = solde

    def depot(self, somme):
      self.solde += somme

    def retrait(self, somme):
      self.solde -= somme

    def affiche(self):
      return self.solde


compte = CompteBancaire("vgv")
print (compte.solde)
retrait = str(input("Vous souhaitez retirer : "))