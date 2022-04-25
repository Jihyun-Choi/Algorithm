N = int(input())
num = list(map(int, input().split()))
dp1 = [1]*N
dp2 = [1]*N
len=[0]*N
for i in range(N):    
    for j in range(0,i):
        if num[j] < num[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)
num.reverse()
for i in range(N):    
    for j in range(0,i):
        if num[j] < num[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)
dp2.reverse()
for i in range(N):
    len[i]=dp1[i]+dp2[i]
print(max(len)-1)
