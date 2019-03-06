while True:
    try:
        n, q = [int(i) for i in input().split()]
        ni = []
        qi = []
        for i in range(n):
            ni.append(int(input()))
        niord = sorted(ni, reverse=True)
        for i in range(q):
            valor = int(input())
            qi.append(niord[valor - 1])
        for i in qi:
            print(i)
    except EOFError:
        break
