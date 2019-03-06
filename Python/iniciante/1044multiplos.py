linha = input().split(" ")
a, b = linha
a = float(a)
b = float(b)
if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
