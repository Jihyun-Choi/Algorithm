# 1
import sys 
input = sys.stdin.readline

N = int(input())
S=[]
dp=[]
for _ in range(N):
    S.append(int(input()))

dp.append(S[0]) 
dp.append(max(S[0]+S[1],S[1])) 
dp.append(max(S[0]+S[2],S[1]+S[2])) 
for i in range(3,N): 
    dp.append(max(dp[i-2] + S[i] , dp[i-3] + S[i] + S[i - 1]))

print(dp[N-1])

# 2
N = int(input())
S = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(N):
    S[i] = int(input())
dp[0] = S[0]
dp[1] = S[0] + S[1]
dp[2] = max(S[1] + S[2], S[0] + S[2])
for i in range(3, N):
    dp[i] = max(dp[i - 3] + S[i - 1] + S[i], dp[i - 2] + S[i])
print(dp[N - 1])

""" 2579
조건에 따라 배열의 값을 합치기.
마지막 계단을 밟아야하므로, 마지막 계단부터 선택해나가기.
dp[i] = i번째 계단을 밟았을 때, 최댓값

# 1 런타임 오류
"""
