j = int(input())
for i in range(j):
    l = input()
    n1 = int(l[0])
    let = l[1]
    n2 = int(l[2])
    if n1 == n2:
        print(n1*n2)
    elif let.isupper():
        print(n2-n1)
    else:
        print(n1+n2)
