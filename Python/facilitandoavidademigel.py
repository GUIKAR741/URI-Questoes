num=int(input())
b=str(bin(num))[2:]
cont=0
for i in b:
    if '1'==i:
        cont+=1
print('S' if cont==len(b) else 'N')
