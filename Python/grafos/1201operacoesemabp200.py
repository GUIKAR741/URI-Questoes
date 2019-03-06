class Node:
    def __init__(self, elemento):
        self.__elemento = elemento
        self.__esquerda = None
        self.__direita = None
        self.__pai = None

    def getElemento(self):
        return self.__elemento

    def setEsquerda(self, esquerda):
        self.__esquerda = esquerda

    def setDireita(self, direita):
        self.__direita = direita

    def getEsquerda(self):
        return self.__esquerda

    def getDireita(self):
        return self.__direita

    def setPai(self, pai):
        self.__pai = pai

    def getPai(self):
        return self.__pai


def imprimir(no, forma, lista):
    if no is not None:
        if forma == 0:
            lista.append(no.getElemento())
            imprimir(no.getEsquerda(), forma, lista)
            imprimir(no.getDireita(), forma, lista)
        elif forma == 1:
            imprimir(no.getEsquerda(), forma, lista)
            lista.append(no.getElemento())
            imprimir(no.getDireita(), forma, lista)
        else:
            imprimir(no.getEsquerda(), forma, lista)
            imprimir(no.getDireita(), forma, lista)
            lista.append(no.getElemento())


def busca_arv(elemento, no):
    if no is None:
        return None
    elif elemento == no.getElemento():
        return no
    elif elemento < no.getElemento():
        if no.getEsquerda() is None:
            return no
        else:
            return busca_arv(elemento, no.getEsquerda())
    else:
        if no.getDireita() is None:
            return no
        else:
            return busca_arv(elemento, no.getDireita())


def insere(elemento):
    global raiz
    no = busca_arv(elemento, raiz)
    if no is not None:
        if no.getElemento() == elemento:
            return
        else:
            novo = Node(elemento)
            if elemento < no.getElemento():
                novo.setPai(no)
                no.setEsquerda(novo)
            else:
                novo.setPai(no)
                no.setDireita(novo)
    else:
        raiz = Node(elemento)


def busca_remove(pai, atual, elemento):
    global raiz
    if atual is not None:
        if elemento > atual.getElemento():
            busca_remove(atual, atual.getDireita(), elemento)
        else:
            busca_remove(atual, atual.getEsquerda(), elemento)
        if elemento == atual.getElemento():
            if atual == raiz:
                raiz = remove_elemento(atual)
            else:
                if pai is not None:
                    if pai.getDireita() == atual:
                        pai.setDireita(remove_elemento(atual))
                    else:
                        pai.setEsquerda(remove_elemento(atual))


def remove_elemento(atual):
    if atual.getEsquerda() is None:
        return atual.getDireita()
    no1 = atual
    no2 = atual.getEsquerda()
    while no2.getDireita() is not None:
        no1 = no2
        no2 = no2.getDireita()
    if no1 != atual:
        no1.setDireita(no2.getEsquerda())
        no2.setEsquerda(atual.getEsquerda())
    no2.setDireita(atual.getDireita())
    return no2


raiz = None
while True:
    try:
        operacao = input().split()
        if len(operacao) == 1:
            lista = []
            if operacao[0] == 'INFIXA':
                imprimir(raiz, 1, lista)
            elif operacao[0] == 'PREFIXA':
                imprimir(raiz, 0, lista)
            else:
                imprimir(raiz, 2, lista)
            print(' '.join([str(i) for i in lista]))
        else:
            if operacao[0] == 'I':
                insere(int(operacao[1]))
            elif operacao[0] == 'P':
                if busca_arv(int(operacao[1]), raiz).getElemento() == int(operacao[1]):
                    print(int(operacao[1]), 'existe')
                else:
                    print(int(operacao[1]), 'nao existe')
            elif operacao[0] == 'R':
                busca_remove(raiz, raiz, int(operacao[1]))
    except EOFError:
        break
