n, m = map(lambda q: int(q), input().split())
ant1 = []
ant2 = []
pred = dict()
for i in range(n):
    ant1.append(0)
    ant2.append(0)
while m != 0:
    x, y = map(lambda q: int(q), input().split())
    pred[str(y-1)] = x - 1
    m -= 1
x, y = map(lambda q: int(q) - 1, input().split())
ant1[x] = 1
i = x
while i != 0:
    ant1[pred[str(i)]] = 1
    i = pred[str(i)]
ant2[y] = 1
i = y
while i != 0:
    ant2[pred[str(i)]] = 1
    i = pred[str(i)]
cont = 0
for i in range(n - 1, -1, -1):
    if ant1[i] == 1 and ant2[i] == 1:
        cont = i + 1
        break
print(cont)
