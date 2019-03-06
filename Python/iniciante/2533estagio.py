while True:
    try:
        m = int(input())
        ni = []
        ci = []
        for i in range(m):
            n = [int(i) for i in input().split()]
            ni.append(n[0])
            ci.append(n[1])
        soma= [(ni[i]*ci[i]) for i in range(len(ni))]
        print("%.4lf" % (sum(soma)/(sum(ci) * 100)))
    except EOFError:
        break
