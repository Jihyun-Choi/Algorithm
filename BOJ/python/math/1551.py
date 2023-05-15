import sys
input = sys.stdin.readline
N, K = map(int, input().split())
num = list(map(int, input().split(',')))
for _ in range(K):
    temp = [num[i] - num[i-1] for i in range(1, len(num))]
    num = temp
print(*num, sep=',')
