import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())  # 정점의 개수, 간선의 개수
K = int(input())  # 시작 정점
path = [INF]*(V+1)
graph = [[] for _ in range(V + 1)]

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    path[start] = 0

    while heap:
        weight_sum, vertex = heapq.heappop(heap)
        if path[vertex] < weight_sum:
            continue
        for weight, next_node in graph[vertex]: 
            next_weight = weight + weight_sum
            if next_weight < path[next_node]:
                path[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
dijkstra(K)
for i in range(1, V+1):
    print("INF" if path[i] == INF else path[i])
