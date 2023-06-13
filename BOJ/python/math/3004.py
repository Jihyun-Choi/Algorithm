N = int(input())
answer, cnt = 1, 1
for i in range(N):
    answer += cnt
    if i%2 == 0:
        cnt += 1
print(answer)
