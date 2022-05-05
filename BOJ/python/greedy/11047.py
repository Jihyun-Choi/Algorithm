import sys
input = sys.stdin.readline

N, K = map(int, input().split())

M = []
c = 0
for _ in range(N):
    M.append(int(input()))

for i in range(N - 1, -1, -1):
    if K == 0:
        break
    if M[i] > K:  # (1)
        continue
    c += K // M[i]
    K %= M[i]

print(c)

""" 11047
'A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수'라는 조건으로 인해 그리디 알고리즘을 사용할 수 있다.

# (1) 조건문이 존재해도, 존재하지 않아도 결과는 달라지지 않는다.
하지만 존재하지 않는 것이 4ms가 더 빠르다.
사칙연산보다 조건문 연산이 시간이 더 오래걸린다는 사실을 다시금 깨달았다.
연산 속도를 생각하며 어떻게 하면 더 효율적인지를 생각하며 코드를 짜도록 하자.
"""
