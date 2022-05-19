from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    queue = deque()
    queue.append(x)
    visit = [0 for _ in range(N + 1)]
    visit[x] = 1
    cnt = 1
    while queue:
        st = queue.popleft()
        for i in graph[st]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                queue.append(i)
    return cnt

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[j].append(i)
result = []
max_cnt = 0
for i in range(1, N + 1):
    tmp = bfs(i)
    if max_cnt == tmp:
        result.append(i)
    if max_cnt < tmp:
        max_cnt = tmp
        result = []
        result.append(i)
print(*result)

""" 1325
PyPy3으로 제출
"""
