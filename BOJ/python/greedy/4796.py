import sys
input = sys.stdin.readline
i = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    print("Case %d: %d" %(i, (V//P)*L + min(V%P, L)))
    i += 1
