linha = input().split(" ")
a, b, c = linha
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159
triangulo = (a * c) / 2
circulo = (c ** 2) * pi
trapezio = ((a + b) / 2) * c
quadrado = b ** 2
retangulo = a * b
print("TRIANGULO: %.3f\n"
      "CIRCULO: %.3f\n"
      "TRAPEZIO: %.3f\n"
      "QUADRADO: %.3f\n"
      "RETANGULO: %.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))
