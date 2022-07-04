N = int(input())
value = sorted(list(map(int, input().split())))
left, right = 0, N-1
sum = value[left] + value[right]
while left < right:
    answer = value[left] + value[right]
    if abs(sum) > abs(answer):
        sum = answer
        result = [value[left], value[right]]
        if answer == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1
print(result[0], result[1])
