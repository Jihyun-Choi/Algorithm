import sys
import heapq
input = sys.stdin.readline
N = int(input())
answer = []
for i in range(N):
    if i == 0:
        arr = list(map(int, input().split()))
        heapq.heapify(arr)
        answer = arr
    else:
        arr2 = list(map(int, input().split()))
        for j in arr2:
            if answer[0] < j:
                heapq.heappop(answer)
                heapq.heappush(answer, j)
print(answer[0])
