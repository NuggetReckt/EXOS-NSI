def echange(x, y, z):
    return x, y, z == y, z, x


def echange2(x, y, z):
    return x, y, z == z, x, y


print("après échange : ", echange(1, 2, 3), echange2(1, 2, 3))
