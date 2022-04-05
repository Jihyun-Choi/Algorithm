import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
A.sort(key=lambda x: (x[1], x[0]))  # (1)
for i in A:
    print(i[0], i[1])


""" 11651
(1) 첫 번째 원소로 오름차순 정렬하고, 첫 번째 원소가 같은 경우 두 번재 원소로 오름차순 정렬하기

key=lambda x: (-x[0], x[1]) : 첫 번째 원소로 내림차순 정렬하고, 첫 번째 원소가 같은 경우 두 번째 원소로 오름차순 정렬하기
"""
