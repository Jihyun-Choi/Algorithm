# 1
N = int(input())

T=[]
for _ in range(N):
    T.append(list(map(int, input().split())))

for i in range(1,N):
    for j in range(0, i+1):
        if j == 0:
            T[i][j] += T[i-1][j]
        elif j == i:
            T[i][j] += T[i-1][j-1]
        else:
            T[i][j] += max(T[i-1][j-1], T[i-1][j])
print(max(T[N-1]))

# 2 
import sys
input = sys.stdin.readline
n = int(input())
last = [0]
for i in range(n):
    line = [int(v) for v in input().split()]
    now = [0] * len(line)
    now[0] = line[0] + last[0]
    now[-1] = line[-1] + last[-1]
    for i in range(1, len(line)-1):
        now[i] = max(last[i], last[i-1]) + line[i]
    last = now
print(max(last))

""" 1932
# 1 34044 KB	200 ms   2차원 배열
# 2 30840 KB	144 ms   1차원 배열
"""
