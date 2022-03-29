class Pile:
    def __init__(self):
        self.pile = []

    def est_vide(self):
        return self.pile == []

    def empiler(self, e):
        self.pile.append(e)

    def depiler(self):
        elem = self.pile[-1]
        self.pile.remove(elem)
        return elem

    def nb_elements(self):
        return len(self.pile)

    def afficher(self):
        print(self.pile)

def etendre(pile1, pile2):
  nb_elements = pile2.nb_elements()
  for i in range(nb_elements):
    element = pile2.depiler()
    pile1.empiler(element)


def supprime_toutes_occurences(pile, element):
    P2 = pile()
    while not pile.est_vide():
      p = pile.empiler
      if p != element():
        P2.empiler()
        P2.depiler()
    pile.empiler()

pile = Pile()
pile.empiler(4)
pile.empiler(5)
pile.empiler(7)
supprime_toutes_occurences(pile, 5)
pile.afficher()