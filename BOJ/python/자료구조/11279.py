import sys
import heapq
input = sys.stdin.readline

N = int(input())
H = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(H, (-x, x))
    else:
        try:
            print(heapq.heappop(H)[1])
        except:
            print(0)


""" 11279
파이썬에서는 이진트리 기반의 최소 힙 자료구조인 heapq 모듈을 제공한다.
최소 힙인 1927 문제를 먼저 푸는 것이 도움될 것이다.
heapq 모듈은 최소 힙이므로 최대 힙으로 활용하려면 약간의 변형이 필요하다.

힙에 튜플을 원소로 추가/삭제 시 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성된다.
최대 힙을 만들려면 각 값에 대한 우선 순위를 구한 후, (우선 순위, 값) 구조의 튜플을 힙에 추가하거나 삭제하면 된다.
그리고 힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 가져오면 된다.
"""
