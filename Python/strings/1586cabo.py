num = int(input())
while num != 0:
    nom = []
    nume = []
    for i in range(num):
        nom.append(input())
        nume.append(0)
    # for i in range(len(nom)):
    #     for j in nom[i]:
    #         nume[i]+=ord(j)
    # for i in range(len(nom)):
    #     nume[i]*=(i+1)
    meio = (0 + len(nom) - 1) // 2
    print(nom[meio] if num % 2 == 1 else 'Impossibilidade de empate.')
    # print(nom[nume.index(max(nume))])
    num = int(input())
