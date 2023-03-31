N = int(input())
answer = 0
for i in range(1, N+1):
    for j in range(i, N+1):
        if i*j <= N: answer += 1
print(answer)
