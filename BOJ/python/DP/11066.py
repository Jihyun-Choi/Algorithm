# 1  오답
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    K = int(input())
    chapter = list(map(int, input().split()))
    heap = []
    answer = 0
    for i in chapter:
        heappush(heap, i)
    while len(heap) != 1:
        temp1 = heappop(heap)
        temp2 = heappop(heap)
        answer += temp1+temp2
        heappush(heap, temp1+temp2)
    print(answer)


# 2  pypy3제출
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    K = int(input())
    nums = [0]+list(map(int, input().split()))
    sums = [0]*(K+1)
    for i in range(1, K+1):
        sums[i] = sums[i-1]+nums[i]
    dp = [[0]*(K+1) for _ in range(K+1)]
    for i in range(2, K+1):  # 길이
        for j in range(i-1,0,-1):
            dp[j][i] = min([dp[k][i]+dp[j][k-1] for k in range(i, j, -1)]) + sums[i]-sums[j-1]
    print(dp[1][K])
