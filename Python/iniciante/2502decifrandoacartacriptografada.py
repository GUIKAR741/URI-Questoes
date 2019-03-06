while True:
    try:
        c, n=[int(j) for j in input().split()]
        cifra=input()
        troca=input()
        for i in range(n):
            texto=input()
            nova=''
            for j in texto:
                if j.isupper():
                    ind=troca.find(j)
                    ind1=cifra.find(j)
                    if ind!=-1:
                        nova+=cifra[ind]
                    elif ind1!=-1:
                        nova+=troca[ind1]
                    else:
                        nova+=j
                else:
                    ind=troca.find(j.upper())
                    ind1=cifra.find(j.upper())
                    if ind!=-1:
                        nova+=cifra[ind].lower()
                    elif ind1!=-1:
                        nova+=troca[ind1].lower()
                    else:
                        nova+=j.lower()
            print(nova)
        print()
    except EOFError:
        break
