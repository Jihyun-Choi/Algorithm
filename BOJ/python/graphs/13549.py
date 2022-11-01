from collections import deque
graph = [-1] * 100001
def bfs(n, k):
    graph[n] = 0
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            return graph[x]
        for i in (x + 1, x - 1, x * 2):  # 이동 가능한 위치
            if 0 <= i <= 100000 and graph[i] == -1:
                if i == x * 2:
                    graph[i] = graph[x]
                    queue.appendleft(i)  # 순간이동인 경우 가중치가 0 이므로 appendleft()
                else:
                    graph[i] = graph[x] + 1
                    queue.append(i)
N, K = map(int, input().split())
print(bfs(N, K))
