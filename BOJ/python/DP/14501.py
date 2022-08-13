import sys
input = sys.stdin.readline
N = int(input())
consult = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]
for i in range(N-1,-1,-1):
    if i + consult[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(consult[i][1] + dp[i + consult[i][0]], dp[i+1])
print(dp[0])
