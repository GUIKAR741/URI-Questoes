def bissexto(x):
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        return True
    return False


def huluculu(x):
    if x % 15 == 0:
        return True
    return False


def buluculu(x):
    if x % 55 == 0 and bissexto(x):
        return True
    return False


f = True
a = input()
while True:
    try:
        if not f:
            print('\n', end='')
        bi = bissexto(int(a))
        hu = huluculu(int(a))
        bu = buluculu(int(a))
        if not bi and not hu and not bu:
            print("This is an ordinary year.\n", end='')
        else:
            if bi:
                print("This is leap year.\n", end='')
            if hu:
                print("This is huluculu festival year.\n", end='')
            if bu:
                print("This is bulukulu festival year.\n", end='')
        f = False
        a = input()
    except EOFError:
        break

