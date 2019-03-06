import math as m
linha = input().split(" ")
a, b, c = linha
ao = a = float(a)
bo = b = float(b)
co = c = float(c)
ab = a+b
ac = a+c
bc = b+c
aab = m.fabs(a-b)
aac = m.fabs(a-c)
abc = m.fabs(b-c)
if (abc < a < bc)and(aac < b < ac)and(aab < c and a < ab):
    calc = a+b+c
    print("Perimetro = %.1lf" % calc)
else:
    calc = ((a+b)/2)*c
    print("Area = %.1lf" % calc)
