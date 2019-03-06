s = input()
contabit = 0
for i in s:
    if i == '1':
        contabit += 1
if contabit % 2 == 0:
    s += '0'
else:
    s += '1'
print(s)
