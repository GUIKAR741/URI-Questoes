receber1 = input().split(" ")
receber2 = input().split(" ")
cod1, num1, val1 = receber1
cod2, num2, val2 = receber2
valor = (float(val1) * int(num1) + float(val2) * int(num2))
print("VALOR A PAGAR: R$ %.2lf" % valor)
