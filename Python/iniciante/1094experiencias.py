c = r = s = t = 0
n = int(input())
while n:
    a, tipo = input().split(" ")
    a = int(a)
    if tipo == "C":
        c += a
    elif tipo == "R":
        r += a
    elif tipo == "S":
        s += a
    t += a
    n -= 1
print("Total: %d cobaias"
      "Total de coelhos: %d"
      "Total de ratos: %d"
      "Total de sapos: %d"
      "Percentual de coelhos: %.2lf %%"
      "Percentual de ratos: %.2lf %%"
      "Percentual de sapos: %.2lf %%" % ((c + r + s), c, r, s, (100.0 * c / t), (100.0 * r / t), (100.0 * s / t)))
