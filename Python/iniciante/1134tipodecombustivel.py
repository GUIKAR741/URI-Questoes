a = g = d = 0
x = 0
while x != 4:
    x = int(input())
    if x == 1:
        a += 1
    elif x == 2:
        g += 1
    elif x==3:
        d += 1
print(("MUITO OBRIGADO\n"
       "Alcool: %d\n"
       "Gasolina: %d\n"
       "Diesel: %d") % (a, g, d))
