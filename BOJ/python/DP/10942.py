# 1 : 시간초과
N = int(input())
nums = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    word = nums[S-1:E]
    if word == word[::-1]:
        print(1)
    else:
        print(0)


# 2 : 2268ms
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
dp = [[0 for _ in range(N)] for _ in range(N)]

for j in range(N):
    for i in range(j+1):
        if i == j : dp[i][j] = 1
        elif i+1 == j :
            if nums[i] == nums[j]: dp[i][j] = 1
            else: dp[i][j] = 0
        elif dp[i+1][j-1] and nums[i] == nums[j]: dp[i][j] = 1
        else: dp[i][j] = 0

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])


# 3 : 2324ms
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
dp = [[0 for _ in range(N)] for _ in range(N)]

for j in range(N):
    for i in range(j+1):
        if i == j : dp[i][j] = 1
        elif i+1 == j :
            if nums[i] == nums[j]: dp[i][j] = 1
        elif dp[i+1][j-1] and nums[i] == nums[j]: dp[i][j] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])
