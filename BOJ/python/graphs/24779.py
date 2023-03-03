import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(R):
    global cnt
    visited[R] = cnt
    for idx in graph[R]:
        if visited[idx] == 0:
            cnt += 1
            dfs(idx)

N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for lst in graph:
    lst.sort()
visited = [0]*(N+1)
stack = [R]
visited[R] = 1
cnt = 1

dfs(R)
for i in range(1,N+1):
    print(visited[i])
