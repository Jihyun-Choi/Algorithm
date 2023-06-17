import sys
input = sys.stdin.readline
for _ in range(int(input())):
    answer = float(input())
    print("$%.2f" % round(answer*0.8, 2))
