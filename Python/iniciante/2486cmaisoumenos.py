vitC = {'suco de laranja': 120,
        'morango fresco': 85,
        'mamao': 85,
        'goiaba vermelha': 70,
        'manga': 56,
        'laranja': 50,
        'brocolis': 34}
n=int(input())
while n!=0:
    vit=0
    for i in range(n):
        esc=input()
        num=int(esc.split()[0])
        for i in range(len(esc)):
            if esc[i]==' ':
                esc=esc[i+1:]
                break
        vit+=vitC[esc]*num
    if vit > 130:
        print("Menos "+str(vit-130)+" mg")
    elif vit < 110:
        print("Mais "+str(110-vit)+" mg")
    else:
        print(str(vit)+" mg")
    n=int(input())
