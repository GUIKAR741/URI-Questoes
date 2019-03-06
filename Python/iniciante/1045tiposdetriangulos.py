import math as m
linha = input().split(" ")
a, b, c = linha
a = float(a)
b = float(b)
c = float(c)
if a < c:
    tmp = c
    c = a
    a = tmp
if a < b:
    tmp = b
    b = a
    a = tmp
if b < c:
    tmp = c
    c = b
    b = tmp
if a >= b+c:
    print("NAO FORMA TRIANGULO")
else:
    if m.pow(a, 2) == m.pow(b, 2) + m.pow(c, 2):
        print("TRIANGULO RETANGULO")
    if m.pow(a, 2) > m.pow(b, 2) + m.pow(c, 2):
        print("TRIANGULO OBTUSANGULO")
    if m.pow(a, 2) < m.pow(b, 2) + m.pow(c, 2):
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("TRIANGULO ISOSCELES")
