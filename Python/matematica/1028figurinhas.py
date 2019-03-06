def mdc(m, n):
    return mdc(n, m % n) if n != 0 else m


i = int(input())
while i > 0:
    i -= 1
    a, b = sorted([int(j) for j in input().split()], reverse=True)
    print(mdc(a, b))
