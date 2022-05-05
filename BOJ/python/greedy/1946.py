import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    n = int(input())
    empoly = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(n):
        empoly.append(list(map(int, input().split())))
    sorted(empoly)
    t = 0
    cnt = 1
    for i in range(1,n):
        if empoly[i][1] < empoly[t][1]:
            t = i
            cnt += 1
    print(cnt) 
