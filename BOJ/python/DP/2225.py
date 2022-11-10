N, K = map(int, input().split())
dp = [[0] * 201 for _ in range(201)]  # 가로:N, 세로:K
for i in range(201):
    dp[i][1] = 1
for i in range(1, 201):
    dp[1][i]=i
    for j in range(2,201):
        dp[j][i] = dp[j][i-1] + dp[j-1][i]
print(dp[N][K] % 1000000000)
