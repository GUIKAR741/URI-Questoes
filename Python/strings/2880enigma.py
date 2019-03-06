cifrada = input()
crib = input()
i = 0
cont = 0
lcif = len(cifrada)
lcrib = len(crib)
while i <= lcif-lcrib:
    cpal = 0
    parteCif = cifrada[0 + i:lcrib + i]
    for j in range(lcrib):
        if crib[j] == parteCif[j]:
            break
        cpal += 1
    if cpal == lcrib:
        cont += 1
    i += 1
print(cont)
