import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    num = input()
    test = str(int(num) + int(num[::-1]))
    if test == test[::-1]: print("YES")
    else: print("NO")
