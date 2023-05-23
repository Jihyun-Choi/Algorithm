import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    dp = [num[0]]
    for i in range(1, N):
        dp.append(max(dp[i-1]+num[i], num[i]))
    print(max(dp))
