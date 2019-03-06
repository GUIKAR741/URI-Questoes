while True:
    try:
        n, d = [int(j) for j in input().split()]
        datasepessoas = []
        for i in range(d):
            datasepessoas.append(input().split())
        podem = []
        for i in datasepessoas:
            contaPodem = 0
            for j in i[1:]:
                if j == '1':
                    contaPodem += 1
            if contaPodem == n:
                podem.append(i)
        podem.sort()
        nova = []
        for i in podem:
            nova.append([int(j) for j in i[0].split('/')])
            # print(i[0], '', '', end='')
        nova.sort(key=lambda a: a[2])
        nn = []
        for i in range(len(nova)):
            if nova[0][2] == nova[i][2]:
                nn.append(nova[i])
        nn.sort(key=lambda a: a[1])
        # print(nn)
        mm = []
        for i in range(len(nn)):
            if nn[0][1] == nn[i][1]:
                mm.append(nn[i])
        max = 32
        data = ''
        # print(mm)
        for i in mm:
            if i[0] < max:
                max = i[0]
                data = '/'.join(str(j) for j in i)
        if len(podem) > 0:
            print(data)
        else:
            print("Pizza antes de FdI")
    except EOFError:
        break
