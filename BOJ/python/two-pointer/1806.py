import sys
N, S = map(int, input().split())
num = list(map(int, input().split()))
left, right, sum = 0, 0, 0
length = sys.maxsize
while True:
    if sum >= S:
        length = min(length, right - left)
        sum -= num[left]
        left += 1
    elif sum < S:
        sum += num[right]
        right += 1
    else:
        break
if length == sys.maxsize:
   print(0)
else:
   print(length)
