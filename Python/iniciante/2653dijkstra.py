string=[]
while True:
    try:
        x=input()
        if x not in string:
            string.append(x)
    except EOFError:
        break
print(len(string))
