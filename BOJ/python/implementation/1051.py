N, M = map(int, input().split())
squre = [list(input()) for _ in range(N)]
size = 0
for i in range(N):
    for j in range(M):
        for k in range(min(N, M)):
            if (((i + k) < N) and ((j + k) < M) and
                squre[i][j] == squre[i+k][j] == squre[i][j+k] == squre[i+k][j+k]):
                size = max(size, (k + 1)**2)
print(size)
