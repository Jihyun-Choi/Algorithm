N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
for i in range(1, N+1):
    for n in nums:
        if i%n == 0:
            answer += i
            break
print(answer)
