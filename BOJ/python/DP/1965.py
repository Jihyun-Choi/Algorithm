n = int(input())
box = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(1,n): 
    for j in range(i): 
        if box[j] < box[i] and dp[i] < dp[j] + 1: 
                dp[i] = dp[j] + 1
print(max(dp))
