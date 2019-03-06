a = int(input())
for i in range(a):
    t = input()
    a = ''
    for j, k in enumerate(t):
        c = ord(k)
        if (65 <= c <= 90) or (97 <= c <= 122):
            a += chr(ord(k) + 3)
        else:
            a += k
    a = a[::-1]
    t = ''
    for j in range(len(a)):
        if j >= int(len(a) / 2):
            t += chr(ord(a[j]) - 1)
        else:
            t += a[j]
    print(t)
