def verificaPV(x, y):
    return "p" if x > y else "v"


n = int(input())
s = list(map(lambda x: int(x), input().split()))
x1 = x = ""
cont = 0
for i in range(n - 1):
    if i == 0:
        x1 = x = verificaPV(s[i], s[i + 1])
    else:
        x = verificaPV(s[i], s[i + 1])
        if x1 == x:
            cont = -1
            break
        x1=x
    if s[i] == s[i + 1]:
        cont = -1
        break
    cont += 1
print(1 if cont > 0 else 0)
