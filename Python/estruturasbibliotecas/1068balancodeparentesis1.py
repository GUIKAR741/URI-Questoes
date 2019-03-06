while True:
    try:
        expr=input()
        par=[]
        for i in expr:
            if i == '(':
                par.append(i)
            if i == ')':
                if len(par)>0:
                    if par[-1] == '(':
                        par.pop()
                else:
                    par.append(i)
        print("correct" if len(par)==0 else "incorrect")
    except EOFError:
        break
