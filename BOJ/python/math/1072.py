from math import floor
import sys
input = sys.stdin.readline
X, Y  = map(int, input().split())
Z = floor(100 * Y / X)
low, high = 0, 1000000000

if Z >= 99: 
    print(-1)
else:
    while low <= high:
        mid = (low + high) // 2
        tx, ty = X + mid, Y + mid
        if floor(100 * ty / tx) > Z: 
            high = mid - 1
        else: 
            low = mid + 1
    print(high + 1)

""" 1072
100*(Y/X) 가 아닌, (Y/X)*100은 부동소수점 오차가 발생할 수 있다.
"""
