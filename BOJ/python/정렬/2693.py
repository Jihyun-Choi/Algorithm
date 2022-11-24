T = int(input())
for i in range(T):
    nums = sorted(list(map(int, input().split())))
    print(nums[-3])
