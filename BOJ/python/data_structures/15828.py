import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque()
while True:
    packet = int(input())
    if packet == -1: break
    if packet == 0 and len(queue) != 0: 
        queue.popleft()
    elif packet != 0 and len(queue) < N:
        queue.append(packet)
if len(queue) == 0: print("empty")
else: print(*queue)
