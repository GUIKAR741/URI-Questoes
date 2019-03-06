a = float(input())
if a < 0 or a > 100:
    print("Fora de intervalo")
else:
    if 0 <= a <= 25:
        print("Intervalo [0,25]")
    else:
        if 25 < a <= 50:
            print("Intervalo (25,50]")
        else:
            if 50 < a <= 75:
                print("Intervalo (50,75]")
            else:
                if 75 < a <= 100:
                    print("Intervalo (75,100]")
