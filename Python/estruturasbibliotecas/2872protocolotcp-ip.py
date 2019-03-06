try:
    while input():
        t = True
        num = []
        while t:
            p = input()
            if "Package" not in p:
                break
            p, n = p.split()
            n = int(n)
            num.append(n)
        num.sort()
        for i in num:
            print("Package %.3d" % i)
        print()
except EOFError:
    pass
