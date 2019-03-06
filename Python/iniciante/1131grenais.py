i = vin = vgr = em = tipo = 0
while tipo != 2:
    ine, gr = [int(i) for i in input().split()]
    i += 1
    if ine == gr:
        em += 1
    elif ine > gr:
        vin += 1
    elif ine < gr:
        vgr += 1
    while True:
        print("Novo grenal (1-sim 2-nao)")
        tipo = int(input())
        if tipo == 1 or tipo == 2:
            break
print(("%d grenais\n"
       "Inter:%d\n"
       "Gremio:%d\n"
       "Empates:%d") % (i, vin, vgr, em))
if vin > vgr:
    print("Inter venceu mais")
elif vin < vgr:
    print("Gremio venceu mais")
elif vin == vgr:
    print("Nao houve vencedor")
