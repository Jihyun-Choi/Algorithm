import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
n = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
k = [int(sys.stdin.readline()) for _ in range(K)]
n.sort()
k.sort()
v=0 
temp = []
for bagWeight in k:
    while n and bagWeight >= n[0][0]:
        heapq.heappush(temp, -n[0][1])  # Max heap
        heapq.heappop(n)
    if temp:
        v += heapq.heappop(temp)
    elif not n:
        break
print(-v)
