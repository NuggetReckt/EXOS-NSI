def etendre(pile1, pile2):
    elem = pile2.depiler()
    pile1.empiler(elem)


def supprime_toutes_occurences(pile, element):
    P2 = pile()
    while not pile.estvide():
        p = pile.empiler
        if p != element():
            P2.empiler()
        P2.depiler()
        pile.empiler()
