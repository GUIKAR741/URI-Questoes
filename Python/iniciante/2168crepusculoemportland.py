n=int(input())
quar=[]
for i in range(n+1):
    quar.append(list(map(lambda x: int(x), input().split())))

for i in range(n):
    for j in range(n):
        nCam=0
        if quar[i][j]==1:
            nCam+=1
        if quar[i+1][j]==1:
            nCam+=1
        if quar[i][j+1]==1:
            nCam+=1
        if quar[i + 1][j + 1] == 1:
            nCam += 1
        print('S' if nCam>=2 else 'U', end='')
    print()
