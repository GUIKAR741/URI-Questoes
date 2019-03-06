n = int(input())
s = b = a = s1 = b1 = a1 = 0
while n > 0:
    nome = input()
    num = [int(i) for i in input().split()]
    num1 = [int(i) for i in input().split()]
    s += num[0]
    b += num[1]
    a += num[2]
    s1 += num1[0]
    b1 += num1[1]
    a1 += num1[2]
    n-=1
print("Pontos de Saque: %.2f %%.\nPontos de Bloqueio: %.2f %%.\nPontos de Ataque: %.2f %%." %
      ((s1*100)/s, (b1*100)/b, (a1*100)/a))
