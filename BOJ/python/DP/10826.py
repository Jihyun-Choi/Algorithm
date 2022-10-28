# 1 34372	80
N = int(input())
P = [0, 1, 1]
for i in range(3, N + 1):
    P.append(P[i - 1] + P[i - 2])
print(P[N])

# 2 30840	76
N = int(input())
x, y = 0, 1
for _ in range(N):
    x, y = y, x+y
print(x)
