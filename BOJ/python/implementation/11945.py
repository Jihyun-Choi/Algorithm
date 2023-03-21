N, M = map(int, input().split())
for _ in range(N):
    print(*list(input())[::-1], sep="")
