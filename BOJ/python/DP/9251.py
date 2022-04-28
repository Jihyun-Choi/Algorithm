A = list(input())
B = list(input())
a = len(A)
b = len(B)
dp = [[0] * (b + 1) for i in range(a + 1)]
for i in range(a):
    for j in range(b):
        if A[i] == B[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
print(dp[a][b])
