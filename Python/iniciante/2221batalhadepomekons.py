t = int(input())
for i in range(t):
    bonus = int(input())
    a1, d1, l1 = map(lambda x: int(x), input().split())
    a2, d2, l2 = map(lambda x: int(x), input().split())
    b1 = bonus if l1 % 2 == 0 else 0
    b2 = bonus if l2 % 2 == 0 else 0
    golpe1=(a1+d1)/2+b1
    golpe2=(a2+d2)/2+b2
    if golpe1>golpe2:
        print("Dabriel")
    if golpe1==golpe2:
        print('Empate')
    if golpe1<golpe2:
        print("Guarte")
