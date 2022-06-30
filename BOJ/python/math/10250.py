T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    X, Y = 0, 0
    if N % H == 0:
        Y = H * 100
        X = N // H
    else:
        Y = (N % H) * 100
        X = N // H + 1
    print(Y + X)
