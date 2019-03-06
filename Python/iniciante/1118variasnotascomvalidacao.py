soma = 0
tipo = 0
while tipo != 2:
    i = 0
    while i < 2:
        n = int(input())
        if 0 <= n <= 10:
            soma += n
            i += 1
        else:
            print('nota invalida')
    print("media = %.2lf\n" % soma / 2)
    i=0
    soma=0
    while True:
        print("novo calculo (1-sim 2-nao)")
        tipo=int(input())
        if tipo==1 or tipo==2:
            break
