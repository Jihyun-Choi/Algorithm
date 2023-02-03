N = int(input())
dp = ['SK','CY','SK','SK'] + ['CY']*N
for i in range(4,N):
    if 'CY' in [dp[i-1], dp[i-3], dp[i-4]]:
        dp[i] = 'SK'
print(dp[N-1])
