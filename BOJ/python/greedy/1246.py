import sys
input = sys.stdin.readline
N, M = map(int, input().split())
price = [int(input()) for _ in range(M)]
price.sort(reverse=True)
answer = []
for i in range(min(N, M)):
    answer.append(price[i]*(i+1))
print(price[answer.index(max(answer))], max(answer))
