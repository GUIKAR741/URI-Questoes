num = int(input())
a = b = 1
l = [a, b]
m = []
for i in range(num):
    a += b
    b += a
    l.append(a)
    l.append(b)
for i in range(num):
    m.append(l[i])
m.reverse()
for i in m[:-1]:
    print(str(i) + ' ', sep='', end='')
print(m[-1])
