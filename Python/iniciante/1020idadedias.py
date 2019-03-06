n = int(input())
ano = int(n / 365)
n -= ano * 365
mes = int(n / 30)
n -= int(mes * 30)
dia = n
print("%i ano(s)\n"
      "%i mes(es)\n"
      "%i dia(s)" % (ano, mes, dia))
