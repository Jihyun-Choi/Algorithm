import sys
input = sys.stdin.readline
i = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    elif V%P > L:
        cnt = L + V // P
    else:
        cnt = V % P + V // P
    print("Case %d: %d" %(i, cnt))
    i += 1
