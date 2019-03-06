p = m = 0
for i in range(100):
    n = int(input())
    p += 1
    if n > m:
        m = n
        pp = p
print("%d\n%d" % (m, pp))
