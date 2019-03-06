soma=0
i = 0
while i < 2:
    n = int(input())
    if 0 <= n <= 10:
        soma += n
        i += 1
    else:
        print('nota invalida')
print("media = %.2lf\n" % soma / 2)
