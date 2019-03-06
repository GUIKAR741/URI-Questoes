soma = 0
x = int(input())
y = int(input())
if x > y:
    ma = x
    me = y
else:
    ma = y
    me = x
for i in range(me + 1, ma):
    if i % 2 != 0:
        soma += i
print("%d" % soma)
