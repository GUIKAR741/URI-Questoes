a = int(input())
for i in range(a):
    b = input().split()
    n, m = map(lambda x: int(x), b)
    print(len(str(n ** m)))
