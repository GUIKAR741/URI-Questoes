n = int(input())
ini = out = 0
for i in range(0, n):
    x = int(input())
    if 10 <= x <= 20:
        ini += 1
    else:
        out += 1
print("%d in" % ini)
print("%d out" % out)
