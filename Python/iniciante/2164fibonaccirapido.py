import math as m
n = int(input())
p1 = ((1 + m.sqrt(5)) / 2) ** n
p2 = ((1 - m.sqrt(5)) / 2) ** n
fib = (p1 - p2) / m.sqrt(5)
print("%.1lf" % fib)
