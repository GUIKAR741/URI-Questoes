while True:
    try:
        n, min, max = [int(i) for i in input().split()]
        pode=0
        for i in range(n):
            if min<=int(input())<=max:
                pode+=1
        print(pode)
    except EOFError:
        break
