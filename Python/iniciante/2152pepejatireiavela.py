a = int(input())
for i in range(a):
    h, m, p = map(lambda x: int(x), input().split())
    p="abriu!" if p==1 else "fechou!"
    print("%.2d:%.2d - A porta %s" % (h, m, p))
