import math

a = int(input())
b = int(input())
c = int(input())



delta = b**2 - (4*a*c)

if (delta > 0):
    raiz_1 = (b * -1 + math.sqrt(delta)) / (2*a)
    raiz_2 = (b * -1 - math.sqrt(delta)) / (2*a)
    print(f"Raiz 1: {raiz_1} Raiz 2: {raiz_2}")
else:
    print("Delta negativo")




