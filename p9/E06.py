n = int(input("Tapez un nombre à trois chiffres :"))

c = n // 100
d = (n - c * 100)//10
n = (n - c * 100) % 10
m = 100 * n + 10 * d + c

print(m)
