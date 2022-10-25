import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)] 
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()
