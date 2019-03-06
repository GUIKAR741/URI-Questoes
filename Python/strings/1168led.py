def qtdLed(led):
    if led == '1':
        return 2
    elif led == '2':
        return 5
    elif led == '3':
        return 5
    elif led == '4':
        return 4
    elif led == '5':
        return 5
    elif led == '6':
        return 6
    elif led == '7':
        return 3
    elif led == '8':
        return 7
    elif led == '9':
        return 6
    elif led == '0':
        return 6


a = int(input())
for i in range(a):
    b = input()
    c = 0
    for j in b:
        c += qtdLed(j)
    print(c, 'leds')

# 3
# 115380
# 2819311
# 23456
