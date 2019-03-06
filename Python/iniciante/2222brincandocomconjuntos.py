t=int(input())
while t>0:
    n=int(input())
    mi=[]
    while n>0:
        mi.append(set(int(i) for i in input().split()[1:]))
        n-=1
    q=int(input())
    while q>0:
        op=[int(i) for i in input().split()]
        op[1] -= 1
        op[2] -= 1
        if op[0] == 1:
            print(len(mi[op[1]] & mi[op[2]]))
        elif op[0] == 2:
            print(len(mi[op[1]] | mi[op[2]]))
        q-=1
    t-=1
