from collections import deque
import sys
input = sys.stdin.readline

# 왼쪽, 오른쪽, 뒤, 앞, 아래, 위
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():  # 너비 우선 탐색
    while q:  # q에 요소가 존재할때까지 탐색
        a, b, c = q.popleft()  # 해당 요소를 뺀 후
        visit[c][a][b] = 1  # 방문 처리
        for i in range(6):  # 탐색 
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]
            if 0 <= x < N and 0 <= y < M and 0 <= z < H and tmt[z][x][y] == 0 and visit[z][x][y] == 0:  # 탐색 조건 **
                q.append([x, y, z])  # q에 추가
                tmt[z][x][y] = tmt[c][a][b] + 1  # 토마토 익는 시간
                visit[z][x][y] = 1  # 방문 처리

M, N, H = map(int, input().split())  # 변수 입력
tmt = [[] for _ in range(H)]
visit = [[[0 for i in range(M)] for i in range(N)] for i in range(H)]
q = deque()
isTrue = st = False

# 토마토 위치 입력
for i in range(H):
    for _ in range(N):
        tmt[i].append(list(map(int, input().split())))
# 토마토가 존재할 경우 큐에 추가
for j in range(H):
    for x in range(N):
        for y in range(M):
            if tmt[j][x][y] == 1:
                q.append([x, y, j])
bfs()  # 탐색
max = 0
for z in range(H):  # 탐색 후 토마토 배열에서 가장 큰 값을 찾음
    for x in range(N):
        for y in range(M):
            if tmt[z][x][y] == 0:  # 익지 않은 토마토가 있는 경우
                isTrue = True
            max = max(max, tmt[z][x][y])
if isTrue == True:  # 찾지 못할 경우 -1을 출력
    print(-1)
else:
    print(max - 1)  # 찾을 경우 해당 값에서 -1 하여 출력
