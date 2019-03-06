n = int(input())
pessoa = []
while n > 0:
    nome = input()
    gd = float(input())
    notas = sum(sorted([float(i) for i in input().split()])[1:-1])
    pessoa.append(nome + (" %.2f" % (notas * gd)))
    n -= 1
for i in pessoa:
    print(i)
