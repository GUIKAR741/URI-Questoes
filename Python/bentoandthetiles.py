num = int(input())
eh = 1
if num <= 1:
    eh = 0
d = 2
while eh == 1 and d <= num / 2:
    if num % d == 0:
        eh = 0
    d += 1
print('N' if eh == 1 else 'S')

