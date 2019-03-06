m, n = input().split()
m = int(m)
n = int(n)
l = []
for i in range(m):
    l.append(input().split())
for i in range(m):
    for j in range(n):
        if i - 1 >= 0 and i + 1 < m and j - 1 >= 0 and j + 1 < n:
            if l[i][j] == '42':
                if l[i-1][j]=='7' and l[i-1][j-1]=='7' and l[i-1][j+1]=='7' and \
                        l[i][j-1]=='7' and l[i][j+1]=='7' and \
                        l[i+1][j] == '7' and l[i+1][j-1]=='7' and l[i+1][j+1]=='7':
                    print(i + 1, j + 1)
                    exit(0)
print(0, 0)
