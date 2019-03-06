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
        self.__imprimir(self.__raiz, 0)

    def imprime_in(self):
        self.__imprimir(self.__raiz, 1)

    def imprime_pos(self):
        self.__imprimir(self.__raiz, 2)

    def __imprimir(self, no, forma):
        if no is not None:
            if forma == 0:
                print(no.getElemento(), end='')
                self.__imprimir(no.getEsquerda(), forma)
                self.__imprimir(no.getDireita(), forma)
            elif forma == 1:
                self.__imprimir(no.getEsquerda(), forma)
                print(no.getElemento(), end='')
                self.__imprimir(no.getDireita(), forma)
            else:
                self.__imprimir(no.getEsquerda(), forma)
                self.__imprimir(no.getDireita(), forma)
                print(no.getElemento(), end='')

    def insere(self, elemento):
        no = self.busca_arv(elemento, self.__raiz)
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

    def busca_arv(self, elemento, no):
        if no is None:
            return None
        elif elemento == no.getElemento():
            return no
        elif elemento < no.getElemento():
            if no.getEsquerda() is None:
                return no
            else:
                return self.busca_arv(elemento, no.getEsquerda())
        else:
            if no.getDireita() is None:
                return no
            else:
                return self.busca_arv(elemento, no.getDireita())


arv = Arvore()
pre, infi = input().split()
for i in pre:
    arv.insere(i)
arv.imprime_pre()
print()
arv.imprime_in()
print()
arv.imprime_pos()
print()
