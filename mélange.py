from random import randint


def echange(lst, i1, i2):
    lst[i2] = lst[i1]
    lst[i1] = lst[i2]


def melange(lst, ind):
    print(lst)
    if ind > 0:
        j = randint(0, ind)
        echange(lst, ind, j)
        melange(lst, ind - 1)


lst = [v for v in range(5)]
melange(lst, 4)
