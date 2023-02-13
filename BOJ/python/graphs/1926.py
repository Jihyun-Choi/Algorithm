import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

answer = [0, 0]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            answer[0] += 1
            answer[1] = max(bfs(i,j), answer[1])
print(answer[0])
print(answer[1])
