import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    pw = input().rstrip()
    print("yes") if 9 >= len(pw) >= 6 else print("no")
