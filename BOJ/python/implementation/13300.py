import sys
input = sys.stdin.readlline
n, k = map(int, input().split())
student = [[0]*2 for _ in range(6)]
for _ in range(n):
    x, y= map(int, input().split())
    student[y-1][x-1] += 1
room_num=0
for a in range(6):
    for b in range(2):
        if(student[a][b]%k == 0):
            room_num += [a][b]/k
        else:
            room_num += student[a][b]//k + 1
print(int(room_num))