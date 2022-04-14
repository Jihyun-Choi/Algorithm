import sys
input = sys.stdin.readline

N = [0, 1, 1, 1, 2, 2] 

for i in range(6, 101):
    N.append(N[i-1]+N[i-5])

T = int(input())
for _ in range(T):
    print(N[int(input())])
