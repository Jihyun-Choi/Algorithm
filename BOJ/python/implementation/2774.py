import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    num = list(input())
    print(len(set(list(num)))-1)
