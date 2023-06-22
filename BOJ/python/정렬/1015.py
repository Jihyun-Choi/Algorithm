N = int(input())
nums = list(map(int, input().split()))
nums_sort = sorted(nums)
idx = []
for i in range(N):
    x = nums_sort.index(nums[i])
    idx.append(x)
    nums_sort[x] = -1
print(*idx)
