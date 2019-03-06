while True:
    try:
        n, o=[int(i) for i in input().split()]
        conta=0
        for i in range(n):
            k, l=[int(i) for i in input().split()]
            if k==o and l==0:
                conta+=1
        print(conta)
    except EOFError:
        break
