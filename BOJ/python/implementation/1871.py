import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    L, D = input().split('-') 
    num = 0
    for i in range(3):
        num += (ord(L[i])-65) * 26**(2-i)
    print("nice" if abs(num-int(D)) <= 100 else "not nice")
