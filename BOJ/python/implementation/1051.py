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

# 2
N, M = map(int, input().split())
squre = [list(input()) for _ in range(N)]
size = 0
wide = min(N, M)
for i in range(N):
    for j in range(M):
        for k in range(wide):
            if (((i + k) < N) and ((j + k) < M) and
                squre[i][j] == squre[i+k][j] == squre[i][j+k] == squre[i+k][j+k]):
                size = max(size, (k + 1)**2)
print(size)

# 3
N, M = map(int, input().split())
squre = [list(input()) for _ in range(N)]
size = 0
if N == 1 or M == 1:
    print(1)
else:
    for i in range(N):
        for j in range(M):
            for k in range(min(N, M)):
                if (((i + k) < N) and ((j + k) < M) and
                    squre[i][j] == squre[i+k][j] == squre[i][j+k] == squre[i+k][j+k]):
                    size = max(size, (k + 1)**2)
    print(size)
