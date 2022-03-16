N = int(input())

nums = list(map(int, input().split()))
M = max(nums)
sum = 0

for i in range(N):
    nums[i] = (nums[i]/M) * 100
    sum += nums[i]

print(sum/N)
