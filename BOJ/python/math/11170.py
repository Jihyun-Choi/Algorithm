import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    answer = 0
    N, M = map(int, input().split())
    for i in range(N, M+1):
        answer += str(i).count('0')
    print(answer)
