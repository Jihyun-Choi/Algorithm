N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
A.sort()
for i in range(N):
    x = A[i]
    y = B.pop(B.index(max(B)))

    answer += x * y

print(answer)


""" 1026
배열 A와 B의 각 요소를 각각 곱해 최솟값을 찾는 문제이다. 
배열 A의 가장 큰 값과 배열 B의 가장 작은 값을 차례차례 곱해서 더하면 된다.
A는 재배열 할 수 있지만, B는 재배열 할 수 없으므로 A를 오름차순으로 정렬한 후,
B의 최댓값의 인덱스를 찾아 그 요소를 pop()을 사용하여 찾아 곱하면 된다.
"""
