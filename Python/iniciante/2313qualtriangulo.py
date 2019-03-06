import math

a, b, c = sorted([int(i) for i in input().split()])
if math.fabs(b - c) < a < b + c:
    if a==b==c:
        print("Valido-Equilatero")
    elif a==b!=c or a!=b==c:
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")
    if c*c==(b*b+a*a):
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")
