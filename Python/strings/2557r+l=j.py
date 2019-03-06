def letra(x):
    if x == 'R' or x == 'L' or x == 'J':
        return True
    return False


while True:
    try:
        a = input()
        n1, c = a.split('+')
        n2, n3 = c.split('=')
        if letra(n3):
            print(int(n1)+int(n2))
        elif letra(n2):
            print(int(n3)-int(n1))
        elif letra(n1):
            print(int(n3)-int(n2))
    except EOFError:
        break
