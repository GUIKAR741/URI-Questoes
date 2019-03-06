import bisect


def pesquisa_binaria_bisect(A, item):
    """Implementa pesquisa binária usando bisect."""
    # Encontra o ponto onde o item deveria ser (ou está) inserido.
    o = bisect.bisect_left(A, item)
    # Testa se o item está na lista.
    return o if o < len(A) and A[o] == item else -1


def pesquisa_binaria_recursiva(A, esquerda, direita, item):
    """Implementa pesquisa binária recursivamente."""
    # 1. Caso base: o elemento não está presente.
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # 2. Nosso palpite estava certo: o elemento está no meio do arranjo.
    if A[meio][1] == item:
        # return item
        return meio
    # 3. O palpite estava errado: atualizamos os limites e continuamos a busca.
    elif A[meio][1] > item:
        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else:  # A[meio] < item
        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)


def pesquisa_binaria(A, item):
    """Implementa pesquisa binária iterativamente."""
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] == item:
            return meio
        elif A[meio] > item:
            direita = meio - 1
        else:  # A[meio] < item
            esquerda = meio + 1
    return -1


n, q = input().split()
n = int(n)
q = int(q)
vet = input().split()
vetOrd = []
i = 0
for i in range(len(vet)):
    vet[i] = int(vet[i])
    # vetOrd.append(vet[i])
vetOrd = list(vet)
vetOrd.sort()
for i in range(len(vet)):
    vet[i] = [vet[i], vetOrd[i]]
for i in range(q, 0, -1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    ind = pesquisa_binaria_recursiva(vet, 0, n - 1, y)
    num = 0
    if x == 1:
        if ind + 1 >= n:
            num = vet[0][1]
        else:
            num = vet[ind + 1][1]
    elif x == -1:
        if ind - 1 < 0:
            num = vet[n - 1][1]
        else:
            num = vet[ind - 1][1]
    indN, indV = pesquisa_binaria_recursiva(vet, 0, n - 1, num), pesquisa_binaria_recursiva(vet, 0, n - 1, y)
    vA = vet[indN][0]
    vB = vet[indV][0]
    if x == 1 and y == 5:
        print(vet[indN],'  ',vet[indV])
    if x==1 and y==5:
        print(vA, vB)

    # print(x, y, num,indN,indV)
    print(x,y,vet,' ',end='')
    vet[indN][0], vet[indV][0] = vB, vA
    print(vet)
    # print(vA, vB, vet)
for i in range(len(vet) - 1):
    print(vet[i][0], ' ', end='', sep='')
print(vet[i + 1][0])
