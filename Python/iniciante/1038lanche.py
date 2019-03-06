linha = input().split()
a, b = linha
a = int(a)
b = int(b)
pagar = 0
if a == 1:
    pagar = b * 4
if a == 2:
    pagar = b * 4.5
if a == 3:
    pagar = b * 5
if a == 4:
    pagar = b * 2
if a == 5:
    pagar = b * 1.5
print("Total: R$ %.2lf" % pagar)
