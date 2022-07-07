N = int(input())
num = list([1] + [0] * 9 for _ in range(N))
num[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    for j in range(1, 10):
        num[i][j] = num[i-1][j] + num[i][j-1]

print(sum(num[N-1]) % 10007)
