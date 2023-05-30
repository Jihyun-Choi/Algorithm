# 1 틀린 풀이
N = int(input())
nums = list(map(int, input().split()))
low, high = 1, 1
answer = 0
for i in range(1, N):
    if nums[i-1] <= nums[i]:
        high += 1
    else: high = 1
    if nums[i-1] >= nums[i]:
        low += 1
    else: low = 1
    answer = max(answer, high, low)
print(answer)

# 2
N = int(input())
nums = list(map(int, input().split()))
d_up, d_down = [1]*N, [1]*N
for i in range(1, N):
    if nums[i] <= nums[i-1]:
        d_up[i] = max(d_up[i], d_up[i-1]+1)
    if nums[i] >= nums[i-1]:
        d_down[i] = max(d_down[i], d_down[i-1]+1)
print(max(max(d_up), max(d_down)))
