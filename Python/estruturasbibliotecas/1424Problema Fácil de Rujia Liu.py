while True:
    try:
        n, m = input().split()
        n=int(n)
        m=int(m)
        di=dict()
        li = input().split()
        for i in li:
            di[i]=li.count(i)
        for i in range(m):
            k, v = input().split()
            k=int(k)
            v=int(v)
            cont = 0
            pos = 0
            if k<=di[str(v)]:
                for i in range(len(li)):
                    if int(li[i][0]) == v:
                        cont += 1
                    if cont == k:
                        pos = i + 1
                        break
            print(pos)
    except EOFError:
        break

