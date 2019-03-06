import math as m

while True:
    try:
        d, vf, vg = input().split()
        d = int(d)
        vf = int(vf)
        vg = int(vg)
        c = 12
        raiz = m.sqrt(144 + (d * d))
        tf = c / vf
        tg = raiz / vg
        print('S' if tg <= tf else 'N')
    except EOFError:
        break
