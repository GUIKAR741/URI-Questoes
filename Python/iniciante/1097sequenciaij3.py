i = k = 1
j = n = 7
while i < 10:
    print("I=%d J=%d" % (i, j))
    j -= 1
    k += 1
    if k == 4:
        k = 1
        i += 2
        n += 2
        j = n
