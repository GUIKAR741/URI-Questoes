while True:
    try:
        t=int(input())
        op=[]
        for i in range(t):
            operacao = input().split()
            o= [int(operacao[0])]
            for i in operacao[1].split('='):
                o.append(int(i))
            op.append(o)
        pessoa=[]
        for i in range(t):
            operacao = input().split()
            indice=int(operacao[1])-1
            resul=0
            if operacao[2] == '+':
                resul=op[indice][0]+op[indice][1]
            if operacao[2] == '-':
                resul=op[indice][0]-op[indice][1]
            if operacao[2] == '*':
                resul=op[indice][0]*op[indice][1]
            if operacao[2] == 'I':
                for j in ['+', '-', '*']:
                    st = 'resul=(' + str(op[indice][0]) + j + str(op[indice][1]) + ")"
                    exec(st)
                    if resul == op[indice][2]:
                        pessoa.append(operacao[0])
                        break
                continue
            if resul!=op[indice][2]:
                pessoa.append(operacao[0])
        pessoa.sort()
        if len(pessoa)==0:
            print('You Shall All Pass!')
        elif len(pessoa)==t:
            print('None Shall Pass!')
        else:
            print(' '.join(pessoa))
    except EOFError:
        break
