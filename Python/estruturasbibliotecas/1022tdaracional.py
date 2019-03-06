def fatora(a, b):
    abs_a, abs_b = abs(a), abs(b)
    menor = min(abs_a, abs_b)
    maior = max(abs_a, abs_b)
    divisor = menor
    while divisor > 1:
        if (menor % divisor) == 0:
            if (maior % divisor) == 0:
                return int(a/divisor), int(b/divisor)
        divisor -= 1
    return a, b


n = int(input())
while n > 0:
    num = input().split()
    op = num[3]
    num = [int(num[0]), int(num[2]), int(num[4]), int(num[6])]
    numero1 = numero2 = 0

    if op == '+':
        numero1 = (num[0] * num[3] + num[1] * num[2])
        numero2 = (num[1] * num[3])
    elif op == '-':
        numero1 = (num[0] * num[3] - num[1] * num[2])
        numero2 = (num[1] * num[3])
    elif op == '*':
        numero1 = (num[0] * num[2])
        numero2 = (num[1] * num[3])
    elif op == '/':
        numero1 = (num[0] * num[3])
        numero2 = (num[2] * num[1])
    n1, n2=fatora(numero1, numero2)
    # if numero1 % 2 == 0 and numero2 % 2 == 0:
    print(str(numero1) + '/' + str(numero2) + ' = ' + str(n1) + '/' + str(n2))
    n -= 1
