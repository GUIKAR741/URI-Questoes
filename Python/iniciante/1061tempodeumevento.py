d1 = input().split("Dia ")
d1 = int(d1[1])
tem = input().split(" : ")
h1, m1, s1 = tem
h1 = int(h1)
m1 = int(m1)
s1 = int(s1)
d2 = input().split("Dia ")
d2 = int(d2[1])
tem = input().split(" : ")
h2, m2, s2 = tem
h2 = int(h2)
m2 = int(m2)
s2 = int(s2)
d1 = d2-d1
h1 = h2-h1
m1 = m2-m1
s1 = s2-s1
if s1 < 0:
    s1 += 60
    m1 -= 1
if m1 < 0:
    m1 += 60
    h1 -= 1
if h1 < 0:
    h1 += 24
    d1 -= 1
print("%d dia(s)" % d1)
print("%d hora(s)" % h1)
print("%d minuto(s)" % m1)
print("%d segundo(s)" % s1)
