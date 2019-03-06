n = int(input())
while n:
    x, y, z = input().split(" ")
    x = float(x)
    y = float(y)
    z = float(z)
    print("%.1lf" % ((x * 2 + y * 3 + z * 5) / 10))
    n -= 1
