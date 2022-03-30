import sys
import heapq
input = sys.stdin.readline

N = int(input())
H = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(H, (abs(x), x))
    else:
        try:
            print(heapq.heappop(H)[1])
        except:
            print(0)
