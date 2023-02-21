import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())  # 노드, 간선
indegree = [0] * (N + 1)  # 진입 차수
graph = [[] for _ in range(N + 1)]  # 간선

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

def topology_sort():
    answer = []
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        answer.append(node)
        for x in graph[node]:
            indegree[x] -= 1
            if indegree[x] == 0:
                queue.append(x)
    print(*answer)
topology_sort()
