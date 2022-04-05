# 1
N = int(input())
A = []

for _ in range(N):
    x, y = map(int, input().split())
    A.append([x, y])
A.sort()
for i in range(N):
    print(A[i][0], A[i][1])


# 2
import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(tuple(map(int, input().split())))

A = sorted(A)

for x, y in A:
    print(x, y)

# 3 (참고코드)
for i in sorted([[*map(int,s.split())]for s in open(0)][1:]):print(*i)

""" 11650
#1의 시간은 4564ms이고, #2의 시간은 400ms이고, #3의 시간은 360ms이다.
#1의 코드에서 입력 코드인 input() -> sys.stdin.readline()으로만 바꿔도 4564->488ms로 바뀐다.
#3은 파이썬 언어중에 가장 짧은 코딩이다... 숏코딩의 세계란...
"""
