# 1
import sys

N = int(input())
num = []  # (1)

for _ in range(N):
    num.append(int(sys.stdin.readline().strip()))

num.sort(reverse=True)

for i in num:
    print(i)


# 2
print(*sorted([int(sys.stdin.readline()) for _ in range(int(input()))], reverse = True))

# 3
input = sys.stdin.readline
n, *L = map(int, open(0))
print(*sorted(L, reverse = True))

# (1)
num = [int(input()) for _ in range(N)]

""" 11931
내림차순으로 정렬하는 방법
1. list.sort(reverse=True)
    내림차순으로 정렬하기
2. reversed(sorted(list))
    오름차순으로 정렬 후 reversed() 함수를 사용하여 리스트의 순서를 거꾸로 출력
"""
