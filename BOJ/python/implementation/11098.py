N = int(input())
for _ in range(N):
    money = []
    player = []
    P = int(input())
    for _ in range(P):
        x, y = map(str, input().split())
        money.append(int(x))
        player.append(y)
    print(player[money.index(max(money))])
