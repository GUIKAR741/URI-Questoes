while True:
    try:
        n = int(input())
        treinos = []
        media=0
        for i in range(n):
            n, m = [int(j) for j in input().split()]
            if m/n>media:
                print(i+1)
                media=m/n
    except EOFError:
        break
