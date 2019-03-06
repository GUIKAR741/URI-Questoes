linha = input().split(" ")
a, b, c = linha
ao = a = int(a)
bo = b = int(b)
co = c = int(c)
if a > c:
    tmp = c
    c = a
    a = tmp
if a > b:
    tmp = b
    b = a
    a = tmp
if b > c:
    tmp = c
    c = b
    b = tmp
print("%i\n%i\n%i\n\n%i\n%i\n%i" % (a, b, c, ao, bo, co))
