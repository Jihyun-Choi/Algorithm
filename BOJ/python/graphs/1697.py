from collections import deque
visited = [0]*100001
def bfs(N, K):
    queue = deque([N])
    visited[N] = 1
    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]-1
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000 and visited[i]==0:
                queue.append(i)
                visited[i] = visited[x]+1    

N, K = map(int, input().split())
print(bfs(N, K))
