while True:
    try:
        n=int(input())
        pala=[]
        while n>0:
            pala.append(input())
            n-=1
        n = int(input())
        while n > 0:
            palavra=input()
            k=j=0
            for i in pala:
                if palavra in i:
                    k+=1
                    if j<len(i):
                        j=len(i)
            if k!=0:
                print(k, j)
            else:
                print(-1)
            n -= 1
    except EOFError:
        break
