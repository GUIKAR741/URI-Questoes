n=int(input())
for i in range(n):
    tipo=input()
    cores=[int(i) for i in input().split()]
    if tipo=='min':
        print("Caso #"+str(i+1)+": "+str(min(cores)))
    elif tipo=='max':
        print("Caso #"+str(i+1)+": "+str(max(cores)))
    elif tipo=='mean':
        print("Caso #"+str(i+1)+": "+str(sum(cores)//len(cores)))
    elif tipo=='eye':
        print("Caso #"+str(i+1)+": "+str(int(0.3*cores[0]+0.59*cores[1]+0.11*cores[2])))
