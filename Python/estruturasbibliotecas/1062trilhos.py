def resolve(n, ent):
    ultimo = n
    pilha1 = []
    for i in ent:
        if ultimo == i:
            ultimo -= 1
            while len(pilha1) > 0:
                if pilha1[-1] == ultimo:
                    pilha1.pop()
                    ultimo -= 1
                else:
                    break
        else:
            pilha1.append(i)
    if ultimo == 0:
        print("Yes")
    else:
        print("No")


num = int(input())
while num != 0:
    entrada = [int(x) for x in input().split()]
    entrada = entrada[::-1]
    while entrada != [0]:
        resolve(num, entrada)
        entrada = [int(x) for x in input().split()]
        entrada = entrada[::-1]
    print()
    num = int(input())
