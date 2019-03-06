risada = input()
vog=''
vogais = ['a', 'e', 'i', 'o', 'u']
conta=0
for i in risada:
    if i in vogais:
        vog+=i
j=len(vog)-1
for i in range(len(vog)):
    if vog[i]==vog[j]:
        conta+=1
    j-=1
if conta==len(vog):
    print('S')
else:
    print('N')
