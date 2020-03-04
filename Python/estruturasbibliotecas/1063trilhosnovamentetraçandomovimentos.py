def resolve(ent, sai):
    pilha1 = []
    for i in ent:
        pilha1.append(i)
        print('I', end='')
        while len(sai) > 0 and len(pilha1) > 0 and pilha1[-1] == sai[0]:
            sai.pop(0)
            pilha1.pop()
            print("R", end='')
    if len(pilha1) > 0:
        print(" Impossible")
    else:
        print()


num = int(input())
while num != 0:
    trem = input().split()
    saida = input().split()
    resolve(trem, saida)
    num = int(input())
