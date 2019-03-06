import math as m

n = int(input())
min = n / m.log(n, m.e)
max = 1.25506 * min
print("%.1f %.1f" % (min, max))
