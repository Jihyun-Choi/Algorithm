num = sorted(list(map(int, input().split())))
if num[1] - num[0] == num[2] - num[1]:
    print(num[2] * 2 - num[1])
elif num[1] - num[0] > num[2] - num[1]:
    print(num[1] * 2 - num[2])
else:
    print(num[1] * 2 - num[0])
