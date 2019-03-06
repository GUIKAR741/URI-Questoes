def comp(x, y):
    l = len(x)
    c = 0
    for i in x:
        if x[i] == y[i]:
            c += 1
    if c == l:
        return True
    return False


n, m = input().split()
n = int(n)
m = int(m)
di = dict()
for i in range(m):
    di[str(i + 1)] = False
x = input().split()
x.__delitem__(0)
for i in x:
    di[i] = not di[i]
ini = dict(di)
fals = dict(ini)
for i in fals:
    fals[i] = False
l = list()
for i in range(n):
    mn = input().split()
    mn.__delitem__(0)
    l.append(mn)
cont = 0
cond = True
x = True
while x:
    for i in l:
        cont += 1
        for j in i:
            di[j] = not di[j]
        if comp(di, fals):
            x = False
            break
    if comp(di, ini):
        cont = -1
        x = False
print(cont)

# 6 3
# 2 1 3
# 3 1 2 3
# 2 1 3
# 2 1 2
# 2 2 3
# 1 2
# 3 1 2 3
