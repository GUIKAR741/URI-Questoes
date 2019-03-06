i=int(input())
tabuleiro=[0]*i
tabuleirofim=[0]*i
for i in range(len(tabuleiro)):
    tabuleiro[i]=int(input())
for i in range(len(tabuleiro)):
    if i == len(tabuleiro) - 1:
        tabuleirofim[i] += tabuleiro[i - 1]+tabuleiro[i]
    elif i>0:
        tabuleirofim[i]+=tabuleiro[i-1]+tabuleiro[i+1]+tabuleiro[i]
    else:
        tabuleirofim[i]+=tabuleiro[i+1]+tabuleiro[i]
for i in tabuleirofim:
    print(i)
