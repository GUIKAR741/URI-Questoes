linha = input().split(" ")
horaini, minutoini, horafim, minutofim = linha
horaini = float(horaini)
minutoini = float(minutoini)
horafim = float(horafim)
minutofim = float(minutofim)
tempo = horafim-horaini
if tempo < 0:
    tempo += 24
tempomin = minutofim-minutoini
if tempomin < 0:
    tempomin += 60
    tempo -= 1
if horaini == horafim and minutoini == minutofim:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (tempo, tempomin))
