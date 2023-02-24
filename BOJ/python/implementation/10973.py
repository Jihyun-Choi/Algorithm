N = int(input())
permut = list(map(int, input().split()))
for i in range(N-1, 0, -1):
    if permut[i-1] > permut[i]:
        for j in range(N-1, 0, -1):
            if permut[i-1] > permut[j]:
                permut[i-1], permut[j] = permut[j], permut[i-1]
                permut = permut[:i] + sorted(permut[i:],reverse=True)
                print(*permut)
                exit()
print(-1)
