x, y = input().split(" ")
x = int(x)
y = int(y)
while 1:
    if x <= 0 or y <= 0:
        break
    if x < y:
        mx = x
        my = y
    else:
        mx = y
        my = x
    soma = 0
    for i in range(mx, my + 1):
        print("%d " % i, end="")
        soma += i
    print("Sum=%d\n" % soma)
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
