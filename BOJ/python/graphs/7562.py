from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(sx, sy, ax, ay):
    queue = deque()
    queue.append([sx, sy])
    s[sx][sy] = 1
    while queue:
        a, b = queue.popleft()
        if a == ax and b == ay:
            print(s[ax][ay] -1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < N and s[x][y] == 0:
                queue.append([x, y])
                s[x][y] = s[a][b] + 1
T = int(input())
for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    s = [[0] * N for _ in range(N)]
    bfs(sx, sy, ax, ay)
