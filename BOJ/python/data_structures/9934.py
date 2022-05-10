import sys
input = sys.stdin.readline
N = int(input())
T = list(map(int, input().split()))
CBT = [[] for _ in range(N)]

def InOrder(list, x):
    mid = (len(list)//2)
    CBT[x].append(list[mid])
    if len(list) == 1:
        return
    InOrder(list[:mid], x+1)
    InOrder(list[mid+1:], x+1)

InOrder(T, 0)
for i in range(N):
    print(*CBT[i])

""" 9934
전위 순회 : 루트 - 왼쪽 자식 - 오른쪽 자식
중위 순회 : 왼쪽 자식 - 루트 - 오른쪽 자식
후위 순회 : 왼쪽 자식 - 오른쪽 자식 - 루트

상근이는 중위 순회로 빌딩들을 방문하여 종이에 적었다.
"""
