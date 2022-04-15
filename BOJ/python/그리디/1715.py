import heapq
import sys

N = int(input())
card = []
for _ in range(N):
    heapq.heappush(card, int(sys.stdin.readline()))


if len(card) == 1:
    print(0)
else:
    answer = 0
    while len(card) > 1:
        temp_1 = heapq.heappop(card)
        temp_2 = heapq.heappop(card)
        answer += temp_1 + temp_2
        heapq.heappush(card, temp_1 + temp_2)
    
    print(answer)

""" 1715
카드 묶음에서 가장 작은 값 두개를 합치는 과정을 반복해나가면 된다.
처음에는 리스트로 묶음의 개수를 추가한 후 정렬하여 작은수부터 더해나갈려고 생각하였다.
그렇게 구현하던 중 합친 묶음을 리스트에 추가하고 정렬하고 다시 더하는 과정에서 시간&메모리가 낭비됨을 느꼈다.
그래서 리스트가 아닌 항상 정렬이 되어있고 작은 값을 뺄 수 있는 힙을 사용하여 문제를 해결하였다.
"""
