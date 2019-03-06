def string(aa, bb):
    la = len(aa)
    lb = len(bb)
    m = 0
    for i in range(la):
        for j in range(lb):
            if aa[i] == bb[j]:
                c = 0
                k = 0
                while k + i < la and k + j < lb:
                    if aa[k + i] != bb[k + j]:
                        break
                    c += 1
                    k += 1
                if c > m:
                    m = c
    print(m)


while True:
    try:
        a = input()
        b = input()
        string(a, b)
    except EOFError:
        break
