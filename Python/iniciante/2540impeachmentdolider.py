while True:
    try:
        a=(int(input())/3)*2
        x=input().split()
        vot1=x.count('1')
        print('impeachment' if vot1>=a else 'acusacao arquivada')
    except EOFError:
        break
