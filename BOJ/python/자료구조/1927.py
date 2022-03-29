# 1
import sys
input = sys.stdin.readline

H = [0]

def insert(x):
    H.append(x)
    # 힙 정렬
    
def find():
    if len(H) == 1:
        print(0)
    else:
        print(H[1])
    
    H[1] = H.pop()
    # 힙 정렬

N = int(input().split())
for _ in range(N):
    X = int(input().split())
    if X == 0:
        find()  # 배열에서 가장 작은 값을 출력 후 값을 배열에서 제거
    else:
        insert(X)  # 배열에 x를 추가


# 2
import sys
import heapq
input = sys.stdin.readline

N = int(input())
H = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(H, x)
    else:
        try:
            print(heapq.heappop(H))
        except:
            print(0)


""" 1927
힙 : 우선순위 큐를 위해 만들어진 자료구조로 완전이진트리이다.

우선순위 큐란, FIFO가 아닌 우선순위가 높은 데이터가 먼저 나가는 형태의 자료구조이다.
우선순위 큐는 배열, 연결리스트, 힙으로 구현할 수 있으며, 힙으로 구현하는 것이 가장 효율적이다.
왜냐하면 배열과 연결리스트는 선형 구조의 자료구조이므로 삽입 또는 삭제 연산을 위한 시간복잡도는 O(n)이지만,
힙트리는 완전이진트리 구조이므로 힙트리의 높이는 log₂(n+1)이며, 힙의 시간복잡도는 O(log₂n)이다.

연산
    insert(x) : 우선순위 큐에 요소 x 추가
    remove() : 우선순위 큐에서 가장 우선순위가 높은 요소를 삭제하고 반환
    find() : 우선순위 큐에서 가장 우선순위가 높은 요소를 반환

구현
힙은 일반적으로 배열을 이용하여 구현한다. 완전 이진트리이므로 중간에 비어있는 요소가 없기 때문이다.

- 자식노드를 구하고 싶을 때
    왼쪽 자식노드 index = (부모 노드 index) * 2
    오른쪽 자식노드 index = (부모 노드 index) * 2 + 1
- 부모노드를 구하고 싶을 때
    부모 노드 index = (자식노드 index) / 2

- 삽입 방법 O(log₂n)
    1. 마지막 노드 뒤에 새로운 노드 추가
    2. 추가된 새로운 노드를 부모의 노드와 비교하여 교환
    3. 정상적인 힙트리가 될 때까지 2번을 반복
- 삭제 방법 O(log₂n)
    1. 루트 노드를 삭제 후 마지막 노드를 루트 노드로 이동
    2. 마지막 노드였던 루트 자리에 위차한 노드를 자식 노드와 비교하여 교환
    3. 정상적인 힙트리가 될 때까지 2번을 반복

# 1을 구현하다가 알게되었다. 파이썬에는 heapq 모듈이 있다는 사실을 ...
"""
