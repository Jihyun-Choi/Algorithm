import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    p=p.replace('RR', '')
    queue = deque(arr)
    cnt = 0
    flag = 0
    if n == 0:
        queue = []
    for i in p:
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if cnt%2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")                    
