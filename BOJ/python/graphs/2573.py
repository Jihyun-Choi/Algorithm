# 1
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Y = 0 # 년도

def bfs(x, y):  # 너비 우선 탐색
    queue = deque()
    queue.append([x, y])
    check[x][y] = 0

    while queue:
        x, y = queue.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if check[nx][ny] == -1 and iceberg[nx][ny] != 0: # 빙산 미방문 & 빙산 존재
                    check[nx][ny] = 0 # 빙산을 방문한걸로 체크
                    queue.append([nx,ny])

def decrease(ice): #섬의 숫자 줄이기, 입력 : 섬 배열 - a
    for i in range(1, N-1):
        for j in range(1, M-1):
            n = 0
            if ice[i][j] > 0:
                for z in range(4):        
                    nx = i + dx[z]
                    ny = j + dy[z]
                    if 0 <= nx < N and 0 <= ny < M: 
                        if ice[nx][ny] == 0: # 바다의 개수만큼 빙산 깍기
                            n += 1 # 깍을 빙산의 수 증가
                ice[i][j] = max(ice[i][j] - n, 0)

while True:
    Y += 1
    num = 0 # 빙산의 개수
    check = [[-1]*M for _ in range(N)] # 방문여부
    decrease(iceberg) # 빙산 감소
    for i in range(1, N-1):
        for j in range(1, M-1):
            if iceberg[i][j] > 0 and check[i][j] == -1: 
                bfs(i,j)
                num += 1
    if num >= 2:
        print(Y)
        break
    elif num == 0:
        print(0)
        break

# 2
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Y = 0 # 년도
check = False

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if iceberg[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif iceberg[nx][ny] == 0:
                    count[x][y] += 1
    return 1

while True:
    visited = [[False]*M for _ in range(N)]
    count = [[0]*M for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))

            iceberg[i][j] -= count[i][j]
            if iceberg[i][j] < 0:
                iceberg[i][j] = 0
    
    if len(result) == 0:
        break
    if len(result) >= 2:
        check = True
        break
    Y += 1

if check:        
    print(Y)
else:
    print(0)
