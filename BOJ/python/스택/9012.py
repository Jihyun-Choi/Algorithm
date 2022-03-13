import sys


def valid_ps(ps):
    sum = 0
    
    for i in ps:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            return 
    if sum == 0:
        print("YES")
    else:
        print("NO")
            

N = int(input())

for _ in range(N):
    ps = sys.stdin.readline()
    valid_ps(ps)
