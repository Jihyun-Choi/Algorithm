import sys
input = sys.stdin.readline
L = int(input())
nums = sorted(list(map(int, input().split())))
n = int(sys.stdin.readline())
if n in nums: print(0)
else:
    min, max = 0, 0
    for num in nums:
        if num < n:
            min = num
        elif num > n and max == 0:
            max = num
    print((n-min-1) * (max-n) + (max-n-1))
