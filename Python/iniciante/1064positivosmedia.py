soma = p = 0
for i in range(0, 6):
    n = float(input())
    if n > 0:
        p += 1
        soma += n
print("%i valores positivos" % p)
print("%.1lf" % (soma/p))
