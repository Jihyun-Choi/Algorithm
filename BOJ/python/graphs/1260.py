from collections import deque
import sys
input = sys.stdin.readline


def dfs(v):  # 깊이 우선 탐색
    visited[v] = True
    ans.append(v)

    if not graph[v]:
        return

    for next in graph[v]:
        if not visited[next]:
            dfs(next)


def bfs(v):  # 너비 우선 탐색
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        node = queue.popleft()
        ans.append(node)

        for next in graph[node]:  # node와 연결된 정점 중, 방문하지 않은 정점들을 queue에 추가
            if not visited[next]:
                visited[next] = True
                queue.append(next)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]  # (1)

for _ in range(m):  # (2)
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(n+1):  # (3)
    graph[i].sort()

for i in range(2):  # (4)
    ans = []
    visited = [False] * (n+1)
    visited[0] = True
    if i % 2 == 0:
        dfs(v)
    else:
        bfs(v)
    print(' '.join(map(str, ans)))


""" 1260
(1) 리스트 내포를 사용하여 graph[]에 n+1개의 []를 추가한다.
(2) 간선의 개수만큼 반복하여 입력받은 두 정점을 그래프에 추가한다. 
    '1 2'를 입력받으면 인덱스 1에 2를 추가, 인덱스 2에 1을 추가하는 방식으로 
    graph의 인덱스를 정점이라 할때 인덱스의 값들은 해당 인덱스 정점과 연결된 정점들이다.
(3) 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하므로, 각 정점에 연결된 정점들을 정렬한다.
(4) DFS와 BFS를 출력하기 위해 2번 반복한다. 
    방문여부를 알기위해 n+1개의 visited[]를 만든다.
    탐색한 정점들의 리스트인 ans를 문자열로 바꾼 후 ' '을 기준으로 각 문자열을 합친다.
"""
