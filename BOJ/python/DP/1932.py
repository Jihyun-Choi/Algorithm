N = int(input())

T=[]
for _ in range(N):
    T.append(list(map(int, input().split())))

for i in range(1,N):
    for j in range(0, i+1):
        if j == 0:
            T[i][j] += T[i-1][j]
        elif j == i:
            T[i][j] += T[i-1][j-1]
        else:
            T[i][j] += max(T[i-1][j-1], T[i-1][j])
print(max(T[N-1]))
