# 1 시간초과
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    _ = input()
    see = list(map(int, input().split()))
    _ = input()
    memory = list(map(int, input().split()))
    for i in memory:
        if i in see:
            print(1)
        else:
            print(0)


# 2  1468ms
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    _ = input()
    see = set(map(int, input().split()))
    _ = input()
    memory = list(map(int, input().split()))
    for i in memory:
        if i in see:
            print(1)
        else:
            print(0)
