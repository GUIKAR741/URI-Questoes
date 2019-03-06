import math as m
linha = input().split(" ")
a, b, c = linha
a = int(a)
b = int(b)
c = int(c)
maior = (a + b + m.fabs(float(a) - float(b))) / 2
maior = (maior + c + m.fabs(float(maior) - float(c))) / 2
print("%.0lf eh o maior" % maior)
