# 1 시간초과, O(n^2)
N = int(input())
nums = list(map(int, input().split()))
answer = []
for i in range(N):
    stack = nums[i:]
    NGE = -1
    for j in stack:
        if nums[i] < j:
            NGE = j
            break
    answer.append(NGE)
print(*answer)


# 2 O(n)
N = int(input())
nums = list(map(int, input().split()))
answer = [-1] * N
stack = []
for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)  # index를 저장
print(*answer)
