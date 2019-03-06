n = int(input())
ini = out = 0
for i in range(1, n):
    if i % 2 == 0:
        print("%d^2 = %.0lf" % (i, (pow(i, 2))))
