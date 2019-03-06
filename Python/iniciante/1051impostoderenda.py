salario = float(input())
if 0 <= salario <= 2000:
    print("Isento")
elif 2000 < salario <= 3000:
    salario -= 2000
    print("R$ %.2lf" % (salario * 0.08))
elif 3000 < salario <= 4500:
    salario -= 3000
    print("R$ %.2lf" % ((1000 * 0.08) + (salario * 0.18)))
elif 4500 < salario:
    salario -= 4500
    print("R$ %.2lf" % ((1000 * 0.08) + (1500 * 0.18) + (salario * 0.28)))
