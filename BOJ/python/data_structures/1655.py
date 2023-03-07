# 1 - 시간초과
N = int(input())
nums = [int(input()) for _ in range(N)]
queue = []
for i in nums:
    queue.append(i)
    queue.sort()
    print(queue[(len(queue)-1)//2])


# 2 
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
leftheap = []
rightheap = []
for i in range(N):
    num = int(input())
    if len(leftheap) == len(rightheap):
        heappush(leftheap, -num)
    else:
        heappush(rightheap, num)
    if rightheap and -leftheap[0] > rightheap[0]: 
        heappush(leftheap, -heappop(rightheap))
        heappush(rightheap, -heappop(leftheap))
    print(-leftheap[0])
