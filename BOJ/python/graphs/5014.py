from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 0
    while q:
        v = q.popleft()
        if v == G:
            return visited[G]
        for i in (v+U, v-D):
            if 0 < i <= F and visited[i] == -1:
                visited[i] = 0
                visited[i] = visited[v] + 1
                q.append(i)
    if visited[G] == -1:
        return "use the stairs"

F, S, G, U, D = map(int, input().split())
visited = [-1 for _ in range(F+1)]
print(bfs(S))
