n = int(input())
par = []
impar = []
while n > 0:
    s = int(input())
    if s % 2 == 0:
        par.append(s)
    else:
        impar.append(s)
    n -= 1
par.sort()
impar.sort(reverse=True)
[print(int(i)) for i in par]
[print(int(i)) for i in impar]
