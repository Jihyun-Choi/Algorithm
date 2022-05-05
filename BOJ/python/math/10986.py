N, M = map(int, input().split())
sum = list(map(int, input().split()))
P = [0 for i in range(M)]
presum = 0
P[0] = 1
for i in range(N):
    presum+=sum[i]
    P[presum%M] += 1
ans=0
for i in P:
    ans += i*(i-1)//2
print(ans)
