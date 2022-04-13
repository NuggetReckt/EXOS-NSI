class Bim:
    def __init__(self, nature, surface, prix_moy):
        self.nt = nature
        self.sf = surface
        self.pm = prix_moy

    def estim_prix(self):
        multiplier = 1
        if self.nt == 'maison':
            multiplier = 1.1
        elif self.nt == 'bureau':
            multiplier = 0.8
        return (self.sf * self.pm) * multiplier

    def nb_maison(self, lst):

        return