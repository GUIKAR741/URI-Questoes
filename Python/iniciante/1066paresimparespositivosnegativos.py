P = N = p = n = 0
for i in range(0, 5):
    n = float(input())
    if n % 2 == 0:
        P += 1
    else:
        N += 1
    if n > 0:
        p += 1
    if n < 0:
        n -= 1
print("%d valor(es) par(es)" % P)
print("%d valor(es) impar(es)" % N)
print("%d valor(es) positivo(s)" % p)
print("%d valor(es) negativo(s)" % n)
