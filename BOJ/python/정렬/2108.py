import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
nums_s = Counter(nums).most_common(2)  # 빈도수가 높은 2개 가져오기

print(round(sum(nums) / n))  # 산술평균
print(nums[n // 2])  # 중앙값
if len(nums_s) > 1:  # 최빈값이 여러개있을 때, 두 번째로 작은 값
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])  # 최빈값이 한개일 때
print(nums[-1] - nums[0])  # 범위
