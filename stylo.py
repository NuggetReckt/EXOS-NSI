from class_reservoir import *

class Stylo:

    def __init__(self, couleur):
        self.Reservoir=Reservoir(couleur)

    def getCouleur(self):
        return self.Reservoir.getCouleur()
    
    def setCouleur(self, couleur):
        self.Reservoir.setCouleur(couleur)
        
from stylo import *

pen=Stylo("Rouge")
print(pen.getCouleur())

pen.setCouleur("Bleu")

print(pen.Reservoir.getCouleur())