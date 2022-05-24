import sys
input = sys.stdin.readline
N, M = map(int, input().split())
listen = [input() for _ in range(N)]
see = [input() for _ in range(M)]
answer = list(set(listen) & set(see))
answer.sort()
print(len(answer))
print(''.join(answer), end = '')

""" 1764
listen = [input().split() for _ in range(N)] -> TypeError 런타임에러 발생.
"""
