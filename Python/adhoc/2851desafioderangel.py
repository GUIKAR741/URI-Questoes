def see(u, v):
    if u != a - 1:
        if b[u] < b[v]:
            visi[u] = 1
            resp[u] = b[v]
            respInd[u] = v
        else:
            see(v, v + 1)
            if resp[v] == -1:
                resp[u] = -1
            elif resp[v] > int(b[u]):
                resp[u] = resp[v]
                respInd[u] = v
            else:
                see(u, respInd[v])
            visi[u] = 1
    else:
        visi[u] = 1

try:
    a = int(input())
    visi = [0] * a
    resp = [-1] * a
    respInd = [-1] * a
    b = [int(i) for i in input().split()]
    for i in range(a):
        if visi[i] == 0:
            see(i, i + 1)
    for i in range(a - 1):
        if resp[i] == -1:
            print("* ", end='')
        else:
            print(str(resp[i]) + " ", end='')
    print("*")
except:
    pass

# def num(q):
#     if q != 0:
#         return q
#     else:
#         return '*'
#
#
# def palavra(a, b):
#     for i in range(a):
#         q = 0
#         for j in range(i + 1, a):
#             if b[j] > b[i] and j > i:
#                 q = b[j]
#                 break
#         if i != a - 1:
#             print(num(q), end=' ')
#         else:
#             print(num(q))
#
#
# # while True:
# #     try:
# a = int(input())
# b = input().split()
# palavra(a, b)
# # except EOFError:
# #     break
