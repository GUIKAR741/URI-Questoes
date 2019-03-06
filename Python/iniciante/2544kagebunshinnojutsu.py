while True:
    try:
        print(len(str(bin(int(input())))[2:])-1)
    except EOFError:
        break
