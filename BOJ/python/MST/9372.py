import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
    print(N-1)


""" 9372
문제를 처음 봤을때 나라별 비행기의 존재 여부를 파악해야되나라고 생각하였지만 필요없었다.
문제 조건에 '주어지는 비행 스케줄은 항상 연결 그래프를 이룬다'로 인해 각 나라는 항상 비행기가 있으므로,
가장 적은 종류의 비행기를 타고자하는 것은 '나라 개수 - 1' 이다.

또한 sys.stdin.readline()을 사용하지 않고, input()을 사용 시 시간초과가 발생할 수 있다.
"""
