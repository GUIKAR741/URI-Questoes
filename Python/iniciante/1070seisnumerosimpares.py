a = int(input())
if a % 2 == 0:
    a += 1
    c = 5
    print("%d" % a)
else:
    c = 6
for i in range(0, c):
    a += 2
    print("%d" % a)
