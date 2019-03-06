a = input()
while "-" not in a:
    if 'x' not in a:
        print(str(hex(int(a))).upper().replace("X", 'x'))
    else:
        print(int(a, 16))
    a = input()
