# 1 시간초과
n = int(input())
num = sorted(list(map(int, input().split())))
x = int(input())
cnt = 0
for i in range(n):
    if num[i] > x : continue
    for j in range(n-1, i, -1):   
        if num[j] > x : continue
        if num[i] + num[j] == x:
            cnt += 1
print(cnt)

# 2
n = int(input())
num = sorted(list(map(int, input().split())))
x = int(input())
cnt = 0
left, right = 0, n-1
while left < right:
    sum = num[left] + num[right]
    if sum == x:
        cnt += 1
        left += 1
    elif sum < x:
        left += 1
    else:
        right -= 1
print(cnt)
