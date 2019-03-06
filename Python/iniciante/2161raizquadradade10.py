def raizAproximada(x, s):
    if x == 0:
        return s + 3
    s += 6
    s = 1 / s
    return raizAproximada(x - 1, s)


n = int(input())
print("%.10f" % raizAproximada(n, 0))
