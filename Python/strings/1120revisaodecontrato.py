x, y = [i for i in input().split()]
while x != '0' and y!='0':
    y=y.replace(x, '')
    print(int(y) if y != '' else 0)
    x, y = [i for i in input().split()]
