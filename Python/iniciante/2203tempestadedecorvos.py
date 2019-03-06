while True:
    try:
        xf, yf, xi, yi, v, r1, r2 = [int(i) for i in input().split()]
        x=xi-xf
        y=yi-yf
        dis=(x**2+y**2)**(1/2)+(1.5*v)
        r=r1+r2
        if r>=dis:
            print("Y")
        else:
            print("N")
    except EOFError:
        break
