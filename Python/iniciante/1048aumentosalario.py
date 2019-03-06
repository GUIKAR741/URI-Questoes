salario = float(input())
if 0 <= salario <= 400:
    reajuste = salario * 0.15
    print("Novo salario: %.2lf\n"
          "Reajuste ganho: %.2lf\n"
          "Em percentual: 15 %%" % (salario + reajuste, reajuste))
elif 400 < salario <= 800:
    reajuste = salario * 0.12
    print("Novo salario: %.2lf\n"
          "Reajuste ganho: %.2lf\n"
          "Em percentual: 12 %%" % (salario + reajuste, reajuste))
elif 800 < salario <= 1200:
    reajuste = salario * 0.10
    print("Novo salario: %.2lf\n"
          "Reajuste ganho: %.2lf\n"
          "Em percentual: 10 %%" % (salario + reajuste, reajuste))
elif 1200 < salario <= 2000:
    reajuste = salario * 0.07
    print("Novo salario: %.2lf\n"
          "Reajuste ganho: %.2lf\n"
          "Em percentual: 7 %%" % (salario + reajuste, reajuste))
elif 2000 < salario:
    reajuste = salario * 0.04
    print("Novo salario: %.2lf\n"
          "Reajuste ganho: %.2lf\n"
          "Em percentual: 4 %%" % (salario + reajuste, reajuste))
