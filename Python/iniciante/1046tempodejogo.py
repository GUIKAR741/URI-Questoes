linha = input().split(" ")
horaini, horafim = linha
horaini = float(horaini)
horafim = float(horafim)
tempo = horafim-horaini
if tempo < 0:
    tempo += 24
if horaini == horafim:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU %i HORA(S)" % tempo)
