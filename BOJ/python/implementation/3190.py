from collections import deque

def change(d, c):  # (1)
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

# 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def start():
    direction = 1  # 초기 방향
    time = 1  # 시간
    y, x = 0, 0  # 초기 뱀 위치
    visited = deque([[y, x]])  # 방문 위치
    N[y][x] = 2
    
    while True:
        y, x = y + dy[direction], x + dx[direction]
        
        if 0 <= y < n and 0 <= x < n and N[y][x] != 2:  # 종료 조건이 아닐경우
            if not N[y][x] == 1:  # 사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                N[temp_y][temp_x] = 0  # 꼬리 제거
            N[y][x] = 2  # 뱀의 위치를 2로 표현
            visited.append([y, x])  # 방문 위치 추가
            if time in times.keys():  # 딕셔너리 키값 중에 현재 시간이 있을 경우
                direction = change(direction, times[time])  # 키값의 value로 방향 전환
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time


n = int(input())  # n은 보드의 크기
N = [[0]*n for i in range(n)]  # 보드의 크기만큼 n*n 2차원 배열 선언

K = int(input())  # K는 사과의 개수
for _ in range(K):  # 사과의 개수만큼 N배열에서 사과의 위치를 1로 표현
    x, y = map(int, input().split())
    N[x-1][y-1] = 1
    
L = int(input())  # L은 뱀의 방향 변환 횟수
times = {}  # times 딕셔너리 선언
for i in range(L):  # 뱀의 방향 변한 횟수만큼 딕셔너리 추가
    X, C = input().split()
    times[int(X)] = C  # 시간을 key, 방향을 value로 추가

print(start())


""" 3190
시뮬레이션 문제 : 알고리즘을 풀 때 모든 과정이 제시되어 그 과정을 거쳐 나온 결과를 추론하는 문제
    문제를 이해하는 것은 쉬우나, 코드로 구현하는 것이 많이 어렵다.

(1)
상(0) 우(1) 하(2) 좌(3)라고 생각하자.
왼쪽으로 회전을 하면, "상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0)"으로 -1 된다.
오른쪽으로 회전을 하면, "상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0)"으로 +1 된다.
d의 값이 항상 0,1,2,3 중에 존대하도록 % 연산자를 사용한다.
"""
