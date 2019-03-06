linha = input().split(" ")
n1, n2, n3, n4 = linha
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
med = (n1*2+n2*3+n3*4+n4*1)/10
print("Media: %.1lf" % med)
if med >= 7:
    print("Aluno aprovado.")
elif 5 <= med < 7:
    print("Aluno em exame.")
    exam = float(input())
    print("Nota do exame: %.1lf" % exam)
    med = (med+exam)/2
    if med >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1lf" % med)
else:
    print("Aluno reprovado.")
