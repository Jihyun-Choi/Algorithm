# 1
import sys

N = int(input())
T = [[] for _ in range(N+1)]
parent = [[] for _ in range(N+1)]

for _ in range(N-1):
    i, j = map(int, sys.stdin.readline().split())
    T[i].append(j)
    T[j].append(i)

def dfs(graph, start, parent):
    s = [start]
    
    while s:
        node = s.pop()
        for i in graph[node]:
            parent[i].append(node)
            s.append(i)
            graph[i].remove(node)
    return parent

for i in list(dfs(T, 1, parent))[2:]:
    print(i[0])


# 2
import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)

for _ in range(N-1):
    a , b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    Q = deque()
    Q.append(1)
    visited = [False] * (N+1)
    parents = [0] * (N+1)
    while Q:
        pnode = Q.popleft()
        visited[pnode] = True
        for cnode in graph[pnode]:
            if not visited[cnode]:
                parents[cnode] = pnode
                Q.append(cnode)
    
    return parents

results = bfs()
print("\n".join(map(str, results[2:])))
