import math as m
linha = input().split(" ")
a, b, c = linha
a = float(a)
b = float(b)
c = float(c)
delta = b ** 2 - 4 * a * c
if a != 0:
    if delta >= 0:
        r1 = (-b + m.sqrt(delta)) / (2 * a)
        r2 = (-b - m.sqrt(delta)) / (2 * a)
        print("R1 = %.5lf\nR2 = %.5lf" % (r1, r2))
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")
