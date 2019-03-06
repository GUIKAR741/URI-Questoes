import math as m
linha1 = input().split(' ')
linha2 = input().split(' ')
x1, y1 = linha1
x2, y2 = linha2
distancia = m.sqrt(m.pow(float(x2) - float(x1), 2) + m.pow(float(y2) - float(y1), 2))
print("%.4lf" % distancia)
