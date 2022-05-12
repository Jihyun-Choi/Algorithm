import sys
N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + matrix[i][j]
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1]))

""" 11660
dp[x,y]는 꼭짓점이 [0,0], [x,y]인 직사각형 안에 있는 요소들의 합의 값이다.
"""
