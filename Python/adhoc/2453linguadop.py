frase = input().split()
nf = []
for i in frase:
    for j in range(0, len(i), 2):
        nf.append(i[j + 1])
    nf.append(' ')
print(''.join(nf).strip())
