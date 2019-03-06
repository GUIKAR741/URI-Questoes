def raiz2(repeticoes, valor):
    if repeticoes > 0:
        return raiz2(repeticoes - 1, (1 / (valor + 2)))
    else:
        return valor+1


rep = int(input())
print("%.10lf" % raiz2(rep, 0))
