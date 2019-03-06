class Rena:
    def __init__(self, nome, peso, idade, altura):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura

    def getNome(self):
        return self.nome

    def getPeso(self):
        return self.peso

    def getIdade(self):
        return self.idade

    def getAltura(self):
        return self.altura

    def __str__(self):
        return "%s" % self.nome

    def __repr__(self):
        return "(%s - %s - %s - %s)" % (self.nome, self.peso, self.idade, self.altura)


def percorre(lista, nlista):
    if type(lista) is list:
        for i in lista:
            elem = percorre(i, nlista)
            nlista.append(elem) if elem is not None else nlista
    else:
        return lista


t = int(input())
cen = 1
while t > 0:
    n, m = [int(i) for i in input().split()]
    renas = []
    while n > 0:
        s = input().split()
        nome = s[0]
        peso = int(s[1])
        idade = int(s[2])
        altura = float(s[3])
        ren = Rena(nome, peso, idade, altura)
        renas.append(ren)
        n -= 1
    renas.sort(key=Rena.getPeso, reverse=True)
    renasMesmoPeso = []
    i = 0
    while len(renas) > 0:
        renasMesmoPeso.append([])
        rena = renas[i]
        renasMesmoPeso[-1].append(rena)
        while True:
            naoEncontra = 0
            for j in range(len(renas)):
                if rena.getPeso() == renas[j].getPeso() and rena.getNome() != renas[j].getNome():
                    renasMesmoPeso[-1].append(renas[j])
                    renas.remove(renas[j])
                    naoEncontra += 1
                    break
            if naoEncontra == 0:
                break
        renas.remove(rena)
    for i in renasMesmoPeso:
        i.sort(key=Rena.getIdade)
    renasMesmaIdade = []
    i=0
    for k in renasMesmoPeso:
        while len(k)>0:
            renasMesmaIdade.append([])
            renasMesmaIdade[-1].append(k[i])
            rena = k[i]
            while True:
                cont = 0
                for j in range(len(k)):
                    if rena.getIdade() == k[j].getIdade() and rena.getNome() != k[j].getNome():
                        renasMesmaIdade[-1].append(k[j])
                        k.remove(k[j])
                        cont += 1
                        break
                if cont==0:
                    break
            k.remove(rena)
    for i in renasMesmaIdade:
        i.sort(key=Rena.getAltura)
    renasMesmaAltura = []
    i=0
    for k in renasMesmaIdade:
        while len(k)>0:
            renasMesmaAltura.append([])
            renasMesmaAltura[-1].append(k[i])
            rena = k[i]
            while True:
                cont = 0
                for j in range(len(k)):
                    if rena.getAltura() == k[j].getAltura() and rena.getNome() != k[j].getNome():
                        renasMesmaAltura[-1].append(k[j])
                        k.remove(k[j])
                        cont += 1
                        break
                if cont==0:
                    break
            k.remove(rena)
    for i in renasMesmaAltura:
        i.sort(key=Rena.getNome)
    nlista = []
    percorre(renasMesmaAltura, nlista)
    print("CENARIO {%s}" % cen)
    cont = 1
    for i in nlista:
        if cont <= m:
            print(cont, '-', i)
            cont += 1
    cen += 1
    t -= 1
