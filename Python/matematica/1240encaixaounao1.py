a = int(input())
for i in range(a):
    b, c = input().split()
    b = b[::-1]
    c = c[::-1]
    d = 0
    if len(c) <= len(b):
        for j in range(len(c)):
            if c[j] == b[j]:
                d += 1
    if d == len(c):
        print("encaixa")
    else:
        print("nao encaixa")
