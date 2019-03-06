while True:
    try:
        n, m=[int(i) for i in input().split()]
        mat=[]
        for i in range(n):
            mat.append([9 if i=='1' else 0 for i in input().split()])
        for i in range(n):
            for j in range(m):
                if mat[i][j]!=9:
                    if i-1>=0 and mat[i-1][j]==9:
                        mat[i][j]+=1
                    if i+1<n and mat[i+1][j]==9:
                        mat[i][j]+=1
                    if j-1>=0 and mat[i][j-1]==9:
                        mat[i][j]+=1
                    if j+1<m and mat[i][j+1]==9:
                        mat[i][j]+=1
        for i in range(n):
            for j in range(m):
                print(mat[i][j], end='')
            print()
    except EOFError:
        break
