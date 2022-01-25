from math import pi


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def perimetre(self):
        return round(2*pi*self.rayon, 2)

    def aire(self):
        return round(pi*self.rayon**2, 2)

    def volume(self):
        return round(((4*pi*self.rayon**3)/3), 2)


class Cylindre:
    def __init__(self, rayon, hauteur):
        Cercle.__init__(self, rayon)
        self.hauteur=hauteur

    def volume_cylindre(self):
        return round(self.hauteur * monCercle.aire(), 2)


monCercle=Cercle(3)

print("- Le périmètre de mon cercle est :", monCercle.perimetre())
print("- L'aire de mon cercle est :", monCercle.aire())
print("- Le volume de ma sphère de rayon", monCercle.rayon, "est :", monCercle.volume())

monCylindre=Cylindre(3, 5)
print("- Le volume de mon cylindre de rayon", monCercle.rayon, "est :", monCylindre.volume_cylindre())