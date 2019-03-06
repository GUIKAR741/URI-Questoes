while True:
    try:
        a = input()
        b = ''
        for j in a:
            if (48 <= ord(j) <= 57) or (ord(j) == 111) or (ord(j) == 79) or (ord(j) == 108) or (ord(j) == 32) \
                    or (ord(j) == 44):
                if 48 <= ord(j) <= 57:
                    b += j
                elif (j == 'o') or (j == 'O'):
                    b += '0'
                elif j == 'l':
                    b += '1'
            else:
                b += '99999999999999999999999999'
        print(int(b) if b and int(b) <= 2147483647 else 'error')
    except EOFError:
        break
