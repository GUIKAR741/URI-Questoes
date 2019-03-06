n = int(input())
while n:
    soma = 0
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if x < y:
        mx = x
        my = y
    else:
        mx = y
        my = x
    for i in range(mx+1, my):
        if i % 2 != 0:
            soma += i
    print("%d" % soma)
    n -= 1
