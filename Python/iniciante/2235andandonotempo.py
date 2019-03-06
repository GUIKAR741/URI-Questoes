num = [int(i) for i in input().split()]
duplicatas = []
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            duplicatas.append(num[j])
if len(duplicatas) > 0:
    print('S')
    exit(0)
num.sort()
soma=num[0]+num[1]
if soma==num[2]:
    print('S')
else:
    print('N')
