# 1 
N = int(input())
dp = [0 for _ in range(N+1)]
W = [0 for _ in range(N)]
for i in range(N):
    W[i] = int(input())
dp[0] = W[0]
dp[1] = W[0] + W[1]
dp[2] = max(W[1] + W[2], W[0] + W[2], dp[1])
for i in range(3, N):
    dp[i] = max(W[i]+dp[i-2], W[i]+W[i-1]+dp[i-3], dp[i-1])
print(dp[N-1])

# 2
N = int(input())
dp = [0 for _ in range(N+1)]
W = [0 for _ in range(N)]
for i in range(N):
    W[i] = int(input())
dp[0] = W[0]
if N>1:
    dp[1] = W[0] + W[1]
if N>2:
    dp[2] = max(W[1] + W[2], W[0] + W[2], dp[1])
for i in range(3, N):
    dp[i] = max(W[i]+dp[i-2], W[i]+W[i-1]+dp[i-3], dp[i-1])
print(dp[N-1])

# 3
import sys
input = sys.stdin.readline

N = int(input())
W = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
if N == 1:
    print(W[1])
else:    
    dp[1] = W[1]
    dp[2] = W[1] + W[2]
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 3] + W[i - 1] + W[i], 
                    dp[i - 2] + W[i],
                    dp[i - 1])
    print(max(dp))

""" 2156
계단 오르기랑 비슷한 문제, 차이점은 마지막 인덱스 값의 포함 여부이다.
dp[i]는 i번째 포도주까지 중에서 최대로 마실 수 있는 포도주의 양이다.
3번째 포도주부터 n번째 포도주까지 어떤것을 선택해야 최댓값인지 고르면 된다.
조건이 연속된 3개의 포도주를 선택할 수 없으므로 dp[i]는 w[i-2], w[i-1], w[i] 중에 가장 작은 값을 선택하지 않으면 된다.

# 1 은 런타임에러(IndexError)가 발생한다. 
# 2579번 문제를 풀때도 똑같은 런타임에러가 발생하였고, 원인을 파악하지 못했는데 이번에도 또같은 이유였다.
# 1에서 N의 값이 1이나 2가 될 경우, W[1], W[2]를 찾을 수 없으므로 발생하였던 오류였다. 
# 2와 같이 조건문을 통해 값을 할당하였더니 에러가 발생하지 않았다.
if문을 2개쓰는 것이 맘에들지 않아 # 3와 같이 if-else로 만들었다.
# 3 코드에서 input = sys.stdin.readline 코드를 추가하였더니 시간이 444 ms에서 76 ms로 감소하였다.
"""
