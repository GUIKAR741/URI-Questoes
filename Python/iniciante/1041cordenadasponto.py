linha = input().split(" ")
x, y = linha
x = float(x)
y = float(y)  # type: float
if x == 0 and y == 0:
    # //origem
    print("Origem")
elif x == 0 and y != 0:
    # //eixo x
    print("Eixo Y")
elif x != 0 and y == 0:
    # //eixo y
    print("Eixo X")
elif x > 0 and y > 0:
    # //q1
    print("Q1")
elif x < 0 and y > 0:
    # //q2
    print("Q2")
elif x < 0 and y < 0:
    # //q3
    print("Q3")
elif x > 0 and y < 0:
    # //q4
    print("Q4")
