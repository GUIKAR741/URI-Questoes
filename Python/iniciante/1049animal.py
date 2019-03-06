c1 = "vertebrado"
c11 = "ave"
c12 = "mamifero"
c111 = "carnivoro"
c112 = "onivoro"
c124 = "herbivoro"
a1 = "aguia"
a2 = "pomba"
a3 = "homem"
a4 = "vaca"
c2 = "invertebrado"
c21 = "inseto"
c22 = "anelideo"
c211 = "hematofago"
a5 = "pulga"
a6 = "lagarta"
a7 = "sanguessuga"
a8 = "minhoca"
tipo1 = input()
if tipo1 == c1:
    tipo2 = input()
    if tipo2 == c11:
        tipo3 = input()
        if tipo3 == c111:
            print(a1)
        if tipo3 == c112:
            print(a2)
    elif tipo2 == c12:
        tipo3 = input()
        if tipo3 == c112:
            print(a3)
        if tipo3 == c124:
            print(a4)
if tipo1 == c2:
    tipo2 = input()
    if tipo2 == c21:
        tipo3 = input()
        if tipo3 == c211:
            print(a5)
        if tipo3 == c124:
            print(a6)
    if tipo2 == c22:
        tipo3 = input()
        if tipo3 == c211:
            print(a7)
        if tipo3 == c112:
            print(a8)
