n = int(input())
while n:
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if y != 0:
        print("%.1lf" % (x / y))
    else:
        print("divisao impossivel")
    n -= 1
