n, T = map(int, input().split())
task = list(map(int, input().split()))
sum, cnt = 0, 0
for i in task:
    if sum+i <= T:
        sum += i
        cnt += 1
    else:
        break
print(cnt)
