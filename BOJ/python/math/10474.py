while True:
    X, Y = map(int, input().split())
    if X == Y == 0:
        break
    print(f"{X//Y} {X%Y} / {Y}")
