dicio = {'1': [0, 1],
         '2': [2, 1],
         '3': [4, 2],
         '4': [8, 3],
         '5': [14, 5],
         '6': [24, 8],
         '7': [40, 13],
         '8': [66, 21],
         '9': [108, 34],
         '10': [176, 55],
         '11': [286, 89],
         '12': [464, 144],
         '13': [752, 233],
         '14': [1218, 377],
         '15': [1972, 610],
         '16': [3192, 987],
         '17': [5166, 1597],
         '18': [8360, 2584],
         '19': [13528, 4181],
         '20': [21890, 6765],
         '21': [35420, 10946],
         '22': [57312, 17711],
         '23': [92734, 28657],
         '24': [150048, 46368],
         '25': [242784, 75025],
         '26': [392834, 121393],
         '27': [635620, 196418],
         '28': [1028456, 317811],
         '29': [1664078, 514229],
         '30': [2692536, 832040],
         '31': [4356616, 1346269],
         '32': [7049154, 2178309],
         '33': [11405772, 3524578],
         '34': [18454928, 5702887],
         '35': [29860702, 9227465],
         '36': [48315632, 14930352],
         '37': [78176336, 24157817],
         '38': [126491970, 39088169],
         '39': [204668308, 63245986]}
j = int(input())
for i in range(j):
    k = int(input())
    res = tuple(dicio[str(k)])
    chamada = res[0]
    res = res[1]
    print('fib(' + str(k) + ") = " + str(chamada) + ' calls = ' + str(res))
