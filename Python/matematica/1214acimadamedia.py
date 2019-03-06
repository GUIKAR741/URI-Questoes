k = int(input())
while k > 0:
    k -= 1
    n = [int(i) for i in input().split()]
    n.pop(0)
    med = sum(n) / len(n)
    maiorMed = list(filter(lambda x: x > med, n))
    print("%.3lf%%" % (len(maiorMed) * 100 / len(n)))
