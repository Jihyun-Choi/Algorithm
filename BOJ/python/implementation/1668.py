import sys
input = sys.stdin.readline
N = int(input())
trophy = [int(input()) for _ in range(N)]
left_cnt = right_cnt = left_max = right_max = 0
for n in trophy:
    if n > left_max:
        left_max = n
        left_cnt += 1
for n in trophy[::-1]:
    if n > right_max:
        right_max = n
        right_cnt += 1
print(left_cnt)
print(right_cnt)
