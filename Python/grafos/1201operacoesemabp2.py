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
                novo = Node(elemento)
                if elemento < no.getElemento():
                    novo.setPai(no)
                    no.setEsquerda(novo)
                else:
                    novo.setPai(no)
                    no.setDireita(novo)
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

    def remove(self, elemento):
        self.__busca_remove(self.__raiz, self.__raiz, elemento)

    def __busca_remove(self, pai, atual, elemento):
        if self.__raiz is None:
            return
        if atual is not None:
            if elemento > atual.getElemento():
                self.__busca_remove(atual, atual.getDireita(), elemento)
            else:
                self.__busca_remove(atual, atual.getEsquerda(), elemento)
            if elemento == atual.getElemento():
                if atual == self.__raiz:
                    self.__raiz=self.__remove_elemento(atual)
                else:
                    if pai is not None:
                        if pai.getDireita() == atual:
                            pai.setDireita(self.__remove_elemento(atual))
                        else:
                            pai.setEsquerda(self.__remove_elemento(atual))

    def __remove_elemento(self, atual):
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
            elif operacao[0] == 'POSFIXA':
                lista = arv.imprime_pos()
            print(' '.join([str(i) for i in lista]))
        else:
            if operacao[0] == 'I':
                arv.insere(int(operacao[1]))
            elif operacao[0] == 'P':
                if arv.busca(int(operacao[1])).getElemento() == int(operacao[1]):
                    print(int(operacao[1]), 'existe')
                else:
                    print(int(operacao[1]), 'nao existe')
            elif operacao[0] == 'R':
                arv.remove(int(operacao[1]))
    except EOFError:
        break
