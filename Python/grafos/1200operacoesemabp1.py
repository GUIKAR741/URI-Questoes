class Node:
    def __init__(self, elemento):
        self.__elemento = elemento
        self.__esquerda = None
        self.__direita = None
        self.__pai = None

    def getElemento(self):
        return self.__elemento

    def setEsquerda(self, esquerda):
        if esquerda is not None:
            self.__esquerda = esquerda

    def setDireita(self, direita):
        if direita is not None:
            self.__direita = direita

    def getEsquerda(self):
        return self.__esquerda

    def getDireita(self):
        return self.__direita

    def setPai(self, pai):
        if pai is not None:
            self.__pai = pai

    def getPai(self):
        return self.__pai


class Arvore:
    def __init__(self):
        self.__raiz = None

    def imprime_pre(self):
        lista = []
        self.__imprimir(self.__raiz, 0, lista)
        return lista

    def imprime_in(self):
        lista = []
        self.__imprimir(self.__raiz, 1, lista)
        return lista

    def imprime_pos(self):
        lista = []
        self.__imprimir(self.__raiz, 2, lista)
        return lista

    def __imprimir(self, no, forma, lista):
        if no is not None:
            if forma == 0:
                lista.append(no.getElemento())
                self.__imprimir(no.getEsquerda(), forma, lista)
                self.__imprimir(no.getDireita(), forma, lista)
            elif forma == 1:
                self.__imprimir(no.getEsquerda(), forma, lista)
                lista.append(no.getElemento())
                self.__imprimir(no.getDireita(), forma, lista)
            else:
                self.__imprimir(no.getEsquerda(), forma, lista)
                self.__imprimir(no.getDireita(), forma, lista)
                lista.append(no.getElemento())

    def insere(self, elemento):
        no = self.__busca_arv(elemento, self.__raiz)
        if no is not None:
            if no.getElemento() == elemento:
                return
            else:
                node = Node(elemento)
                if elemento < no.getElemento():
                    node.setPai(no)
                    no.setEsquerda(node)
                else:
                    node.setPai(no)
                    no.setDireita(node)
        else:
            self.__raiz = Node(elemento)

    def __busca_arv(self, elemento, no):
        if no is None:
            return None
        elif elemento == no.getElemento():
            return no
        elif elemento < no.getElemento():
            if no.getEsquerda() is None:
                return no
            else:
                return self.__busca_arv(elemento, no.getEsquerda())
        else:
            if no.getDireita() is None:
                return no
            else:
                return self.__busca_arv(elemento, no.getDireita())

    def busca(self, elemento):
        return self.__busca_arv(elemento, self.__raiz)


arv = Arvore()
while True:
    try:
        operacao = input().split()
        if len(operacao) == 1:
            lista = None
            if operacao[0] == 'INFIXA':
                lista = arv.imprime_in()
            elif operacao[0] == 'PREFIXA':
                lista = arv.imprime_pre()
            else:
                lista = arv.imprime_pos()
            print(' '.join(lista))
        else:
            if operacao[0] == 'I':
                arv.insere(operacao[1])
            else:
                if arv.busca(operacao[1]).getElemento() == operacao[1]:
                    print(operacao[1], 'existe')
                else:
                    print(operacao[1], 'nao existe')
    except EOFError:
        break
