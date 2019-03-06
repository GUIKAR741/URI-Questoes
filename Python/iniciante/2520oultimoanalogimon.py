while True:
    try:
        n, m = [int(i) for i in input().split()]
        lis = []
        pos1 = pos2 = None
        for i in range(n):
            lis.append([])
            ind = input().split()
            j = 0
            for k in ind:
                k = int(k)
                lis[-1].append(k)
                if lis[i][j] == 1:
                    pos1 = (i + 1, j + 1)
                if lis[i][j] == 2:
                    pos2 = (i + 1, j + 1)
                j += 1
        # X
        passos = 0
        if pos1[0] > pos2[0]:
            passos += pos1[0] - pos2[0]
        elif pos1[0] < pos2[0]:
            passos += pos2[0] - pos1[0]
        # Y
        if pos1[1] > pos2[1]:
            passos += pos1[1] - pos2[1]
        elif pos1[1] < pos2[1]:
            passos += pos2[1] - pos1[1]
        print(passos)
    except (EOFError, Exception) as e:
        break
