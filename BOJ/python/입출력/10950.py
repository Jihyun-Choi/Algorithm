# 1
T = int(input())

for i in range(0,T):
    num = input().split()
    print(int(num[0])+int(num[1]))


# 2
import sys

T = int(input())

for i in range(0,T):
    num = sys.stdin.readline().split()
    print(int(num[0])+int(num[1]))