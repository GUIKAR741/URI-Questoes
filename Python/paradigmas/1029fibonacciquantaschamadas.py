from collections import OrderedDict
fib = {
    1: OrderedDict({
        'num': 0,
        'call': 1
    }),
    2: OrderedDict({
        'num': 2,
        'call': 1
    }),
    3: OrderedDict({
        'num': 4,
        'call': 2
    }),
    4: OrderedDict({
        'num': 8,
        'call': 3
    }),
}
for i in range(5, 40):
    fib[i] = OrderedDict({
        'num': fib[i - 1]['num'] + fib[i - 2]['num'] + 2,
        'call': fib[i - 1]['call'] + fib[i - 2]['call']
    })

j = int(input())
for i in range(j):
    k = int(input())
    res = fib[k]
    chamada = res['num']
    res = res['call']
    print('fib(' + str(k) + ") = " + str(chamada) + ' calls = ' + str(res))
