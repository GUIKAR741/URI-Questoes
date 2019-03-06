while True:
    try:
        alfabeto=input()
        letras=int(input())
        men=[]
        n=[int(i) for i in input().split()]
        for i in n:
            men.append(alfabeto[i-1])
        print(''.join(men))
    except EOFError:
        break
