# 1
import sys
input = sys.stdin.readline

V, E = map(int, input().split())

G = []
for i in range(E):
    A, B, C = map(int, input().split())
    G.append([C, A, B])

G.sort(key=lambda x: x[0])

sum = 0
visited = []
for i in range(E):
    if len(visited) == V:
        break
    if G[i][1] in visited and G[i][2] in visited:
        continue
    if G[i][1] not in visited:
        visited.append(G[i][1])
    if G[i][2] not in visited:
        visited.append(G[i][2]) 
    sum += G[i][0]

print(sum)


# 2
import sys, heapq
input = sys.stdin.readline

v,e = map(int,input().split())  # 정점, 간선의 개수 입력
cnt,hq = 0,[]
visit = [0]*(v+1)  # 정점의 방문 여부를 알기위한 배열

# 그래프 구성 - (1)
link = [[] for _ in range(v+1)]  # 인접 리스트로 그래프를 저장
for _ in range(e):  # 양쪽 노드의 인덱스에 (가중치, 연결된 노드)형태인 튜플값으로 link[]에 추가
    a,b,c = map(int,input().split())
    link[a].append((c,b))
    link[b].append((c,a))

# 임의의 정점을 힙에 넣음
visit[1] = 1
for i in link[1]:  # 한 정점에서 갈 수 있는 정점들을 hp[]에 추가
    heapq.heappush(hq,i)

sum = 0
while hq:  # 
    if cnt == v-1:  # 간선이 총 v-1개 이루어졌다면 종료
        break
        
    w,node = heapq.heappop(hq)  # hq의 값을 pop하여 w,node로 할당
    if visit[node]:  # 만약 방문한 노드라면 continue
        continue
    
    cnt+=1  # 현재 간선의 개수
    sum+=w  # 현재 가중치의 합
    visit[node] = 1  # 방문 여부 
    for i in link[node]:  # 방문한 노드와 연결된 노드들 중 방문하지 않은 노드를 hp[]에 추가
        tw,tnode = i
        if visit[tnode]:
            continue
        heapq.heappush(hq,i)
print(sum)


# 3
V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

edges.sort(key=lambda x:x[2])
R = list(range(V+1))
ans = 0

def FR(x):
    if x != R[x]:
        R[x] = FR(R[x])
    
    return R[x]

cnt = 0

for u, v, w in edges:
    if cnt == V-1:
        break

    ru, rv = FR(u), FR(v)

    if ru != rv:
        R[ru] = R[rv] = min(ru, rv)
        ans += w
        cnt += 1

print(ans)

 
""" 1197
MST를 푸는 방법은 프림 알고리즘을 사용하거나, 크루스칼 알고리즘을 사용하는 것이다.
간선의 개수가 작은 경우에는 크루스칼, 간선의 개수가 많은 경우에는 프림을 사용하는 것이 좋다.
이번 문제에서는 프림 알고리즘을 사용하여 풀었다.

프림 알고리즘의 구현은 다음과 같다. 
    1. 그래프의 간선들을 가중치의 오름차순으로 정렬
    2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택
    3. 가장 낮은 가중치를 먼저 선택
    4. 사이클을 형성할 시 간선을 제외
    5. 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가

(1) 그래프의 구현 방법
1. 인접 리스트
    가장 일반적인 방법
    모든 정점을 인접 리스트에 저장. 즉, 각각의 정점에 인접한 정점들을 리스트로 표시
    무방향 그래프에서 간선은 두번 저장된다. 즉, 노드 1과 노드 2가 연결되어있다면 노드 1에 2를, 노드 2에 1을 저장한다.
2. 인접 행렬
    정점의 개수가 N인 그래프를 N*N배열로 표현한다.
    matrix[i][j]가 true라면 i->j로의 간선이 존재한다는 뜻이다.

#1로 처음에 구현하였다가 시관초과...가 되었다. heapq를 사용하여 구현해보았다.
"""
