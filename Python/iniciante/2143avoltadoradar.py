a = int(input())
while a != 0:
    for i in range(a):
        n = int(input())
        if n % 2 == 0:
            print(n * 2 - 2)
        else:
            print(n * 2 - 1)
    a = int(input())
