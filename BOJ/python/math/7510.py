import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    num = sorted(list(map(int, input().split())))
    print('Scenario #%d:'%(i+1))
    if (num[0]**2 + num[1]**2 == num[2]**2):
        print('yes\n')
    else:
        print('no\n')
