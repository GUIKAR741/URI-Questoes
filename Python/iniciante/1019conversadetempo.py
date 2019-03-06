n = int(input())
hora = n / 3600
min = (n % 3600) / 60
seg = (n % 3600) % 60
print("%i:%i:%i" % (hora, min, seg))
