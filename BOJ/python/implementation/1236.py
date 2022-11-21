import sys
input = sys.stdin.readline
N, M = map(int, input().split())
row, col = 0, 0
castle = [input() for _ in range(N)]
for i in range(N):
    if 'X' not in castle[i] :
        row += 1
for j in range(M):
    if 'X' not in [castle[i][j] for i in range(N)]:        
        col += 1
print(max(row, col))
