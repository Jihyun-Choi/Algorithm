# 1
N = int(input())
answer = 0
for i in range(N + 1, N ** 2, N + 1):
    answer += i
print(answer)

# 2
N = int(input())
print((N-1)*N*(N+1)//2)
