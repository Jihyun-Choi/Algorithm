N, M, L = map(int, input().split())
nums = [0]*N
cnt = i = 0
while nums[i] < M-1:
    nums[i] += 1
    cnt += 1
    if nums[i]%2 == 1:
        i = (i+L)%N
    else:
        i = (i-L)%N
print(cnt)
