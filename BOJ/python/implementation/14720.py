N = int(input())
milk = list(map(int,input().split()))
answer = 0
for i in range(N):
    if milk[i] == answer % 3:
        answer += 1
print(answer)
