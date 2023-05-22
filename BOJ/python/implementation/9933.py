import sys
input = sys.stdin.readline
words=[]
for _ in range(int(input())):
    words.append(input())
for qw in words:
    if qw[::-1] in words:
        print(len(qw),qw[len(qw)//2])
        break
