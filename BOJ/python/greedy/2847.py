N = int(input())
score = [int(input()) for _ in range(N)][::-1]
ans = 0
for i in range(N-1):
    if score[i] <= score[i+1]:
        m = score[i+1] - score[i] + 1
        ans += m
        score[i+1] -= m 
print(ans)
