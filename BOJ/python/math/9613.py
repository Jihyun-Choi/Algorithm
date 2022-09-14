import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    sum = 0
    num = list(map(int, input().split()))
    for j in range(1, len(num)):
        for k in range(j+1, len(num)):
            sum += math.gcd(num[j], num[k])
    print(sum)
