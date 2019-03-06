def percorre(lista, nlista):
    if type(lista) is list:
        for i in lista:
            elem = percorre(i, nlista)
            nlista.append(elem) if elem is not None and elem != '' else nlista
    else:
        return lista


q = int(input())
normal = [1, 2, 3, 4, 5, 6]
while q > 0:
    n = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
    nl = [len(i) for i in n]
    nn = []
    nl.sort()
    if nl[0] == 1 and nl[1] == 1 and nl[2] == 4:
        percorre(n, nn)
        nn.sort()
        lados=[0, 0, 0]
        for i in n:
            if len(i)==1:
                lados[0]+=i[0]
            else:
                lados[1]+=i[0]+i[2]
                lados[2]+=i[1]+i[3]
        if lados==[7, 7, 7] and nn==normal:
            print('SIM')
        else:
            print('NAO')
    else:
        print('NAO')
    q -= 1
