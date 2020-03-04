while True:
    try:
        x, y = [int(i) for i in input().split()]
        print(x ^ y)
    except EOFError:
        break
