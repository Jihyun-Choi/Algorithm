# 1
N, M = map(int, input().split())
num = list(map(int, input().split()))
left, right, sum, cnt = 0, 0, 0, 0
while left <= right and right <= len(num): 
    if sum > M:
        if left < right:
            sum -= num[left]
            left += 1 
        else:
            sum -= (num[left] + num[right])
            left += 1
            right += 1
    else:
        if sum == M:
            cnt += 1
        sum += num[right]
        right += 1
print(cnt)

# 2
N, M = map(int, input().split())
num = list(map(int, input().split()))
left, right, sum, cnt = 0, 0, 0, 0
while not (left == right == N):
    if sum < M and right < N:
        sum += num[right]
        right += 1 
    else:
        sum -= num[left]
        left += 1
    if sum == M:
        cnt += 1
print(cnt)


""" 2003
two pointer의 조건은 배열의 원소가 자연수이어야 함.
따라서 right 포인터가 증가하면 부분합은 증가하며, left 포인터가 증가하면 부분합은 감소함.
"""
