n, q = input().split()
n = int(n)
q = int(q)
while True:
    if q==0 and n==0:
        exit(0)
    lamp = [i for i in input()]
    oriLamp = lamp[:]
    while q>0:
        k, m = [int(i) for i in input().split()]
        i = k
        c = 1
        lamp=oriLamp[:]
        lamp[0] = 'o' if lamp[0]=='x' else 'x'
        while lamp != oriLamp:
            lamp[i] = 'o' if lamp[i]=='x' else 'x'
            i = (i + k) % n
            c += 1
        m %= c
        lamp=oriLamp[:]
        while m>0:
            lamp[i] = 'o' if lamp[i]=='x' else 'x'
            i = (i + k) % n
            m-=1
        print(''.join(lamp))
        q-=1
    n, q = map(lambda x: int(x), input().split())
