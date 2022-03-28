# 1
import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
    
for _ in range(M):
    sum = 0
    i, j = map(int, sys.stdin.readline().split())
    for k in range(i-1, j):
        sum += num[k]
    print(sum)

# 2
import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
prefix_sum = []

sum = 0
for i in num:
    sum += i
    prefix_sum.append(sum)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split()) 
    print(prefix_sum[j-1]-prefix_sum[i-2])

# 3 
import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]

sum = 0
for i in num:
    sum += i
    prefix_sum.append(sum)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split()) 
    print(prefix_sum[j]-prefix_sum[i-1])


""" 11659
문제를 처음 본 후 # 1과 같이 구현하였고, 그 결과는 '시간초과'였다.
그제서야 각 반복문마다 일일이 합산을 하여 구하는 것이 적지않은 시간이라는 사실을 깨달았다.
알고리즘을 설계할 때 여러 번 사용될 만한 정보는 미리 구해서 저장해 놓는 것이 좋다.


구간 합 계산 : 연속적으로 나열된 N개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 구하는 문제
수의 개수를 N, 합을 구해야 하는 횟수 M이라고 한다면, 매번 구간 합을 계산 시 O(NM)의 시간복잡도를 가진다.
N과 M의 범위가 커진다면 시간복잡도가 매우 커져 문제를 해결할 수 없다.
이러한 경우, 접두사 합(Prefix Sum) 알고리즘을 사용하여 해결한다.
접두사 합 알고리즘을 사용하면 각 구간 합을 계산 시 O(1)이 되므로 전체 구간 합을 계산하는 시간복잡도는 O(N+M)이다.

접두사 합(Prefix Sum)
1. N개의 수에 대하여 접두사 합(Prefix Sum)을 계산하여 배열 P에 저장한다.
2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간 합은 P[R] - P[L-1]이다.

즉 N = [1, 2, 3, 4, 5]인 N이 주어질 때 PS = [1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5]이다.

# 2
배열의 PS[0] = 0이 되지 않는다면, 인덱스값이 음수가 되어 원하지않는 결과가 나온다.
"""
