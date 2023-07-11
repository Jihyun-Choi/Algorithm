import sys
input = sys.stdin.readline
answer = []
while True:
    try:
        N, S = map(int, input().split())
        answer.append(S // (N+1))
    except:
        print(*answer, sep = '\n')
        break
