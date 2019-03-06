while True:
    try:
        n=int(input())
        m, ll=[int(i) for i in input().split()]
        barM=[]
        barL=[]
        for i in range(m):
            barM.append([int(i) for i in input().split()])
        for i in range(ll):
            barL.append([int(i) for i in input().split()])
        cm, cl=[int(i)-1 for i in input().split()]
        a=int(input())-1
        if barM[cm][a]>barL[cl][a]:
            print("Marcos")
        elif barM[cm][a]<barL[cl][a]:
            print("Leonardo")
        else:
            print("Empate")
    except EOFError:
        break
