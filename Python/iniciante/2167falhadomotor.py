n = int(input())
rpm = list(map(lambda x: int(x), input().split()))
falhas = 0
for i in range(1, len(rpm[1:])+1):
    if rpm[i - 1] > rpm[i]:
        print(i + 1)
        exit(0)
print(0)
