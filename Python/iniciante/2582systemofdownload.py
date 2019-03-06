lista = ['PROXYCITY',
         'P.Y.N.G.',
         'DNSUEY!',
         'SERVERS',
         'HOST!',
         'CRIPTONIZE',
         'OFFLINE DAY',
         'SALT',
         'ANSWER!',
         'RAR?',
         'WIFI ANTENNAS']
n=int(input())
while n>0:
    a=sum([int(i) for i in input().split()])
    print(lista[a])
    n-=1
