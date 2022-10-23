# 1 : 30840KB   80ms
import sys
input = sys.stdin.readline
sum, x, y = -1, 0, 0
for i in range(9):
    arr = list(map(int,input().split()))
    if max(arr) > sum:
        sum, x, y = max(arr), i, arr.index(max(arr))
print(sum)
print(x+1, y+1)

# 2 : 30840KB   68ms
import sys
input = sys.stdin.readline
sum,x,y = -1,0,0
for i in range(9):
    arr = list(map(int,input().split()))
    for j in range(9):
        if arr[j] > sum:
            sum,x,y = arr[j],i,j
print(sum)
print(x+1, y+1)
