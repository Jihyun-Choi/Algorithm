import sys
input = sys.stdin.readline
W, L = map(int, input().split())
width, length = [0, W], [0, L]  # 가로, 세로
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 1: width.append(y)
    else: length.append(y)
width.sort()
length.sort() 
N, M = [], []  # 길이
for i in range(1, len(width)):
    N.append(width[i]-width[i-1])
for j in range(1, len(length)):
    M.append(length[j]-length[j-1])
print(max(N) * max(M))
