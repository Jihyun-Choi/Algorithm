nums = [list(map(int, input().split())) for _ in range(2)]
sums = []
for _ in range(4):
    sums.append((nums[0][0] / nums[1][0]) + (nums[0][1] / nums [1][1]))
    new_nums = [[nums[1][0], nums[0][0]], [nums [1][1], nums[0][1]]]
    nums = new_nums
print(sums.index(max(sums)))
