# 1
import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    
    if (a == b == 0):
        break
    else:
        print(a+b)


# 2
import sys

a, b = map(int, input().split())

while (a+b) != 0:
    print(a+b)
    a, b = map(int, input().split())
