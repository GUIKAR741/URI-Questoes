def verificaPrimo(num):  # Complexidade O(sqrt(n))
    if num == 1:
        return 0
    i = 2
    while i * i <= num:
        if num % i == 0:
            return 0
        i += 1
    return 1


while True:
    try:
        num = int(input())
        eh = verificaPrimo(num)
        ep = 0
        primos = [2, 3, 5, 7]
        for i in str(num):
            if int(i) in primos:
                ep += 1
        if eh == 1 and ep == len(str(num)):
            print('Super')
        elif eh == 1:
            print('Primo')
        else:
            print('Nada')
    except EOFError:
        break
