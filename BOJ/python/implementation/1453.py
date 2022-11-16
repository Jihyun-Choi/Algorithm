N = int(input())
idx = list(map(int, input().split()))
M = len(list(set(idx)))
print(N-M)
