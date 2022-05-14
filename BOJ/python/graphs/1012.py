import sys
from collections import deque
input = sys.stdin.readline

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):  # 너비 우선 탐색
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]    
    for _ in range(K):
        i, j = map(int, input().split())
        graph[i][j] = 1
    cnt = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
