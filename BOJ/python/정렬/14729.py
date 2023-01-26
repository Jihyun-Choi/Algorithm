import sys
input = sys.stdin.readline
N = int(input())
score = [float(input()) for _ in range(N)]
for i in sorted(score)[:7]:
    print("{:.3f}".format(i))
