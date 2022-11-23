def dfs(idx):
    if len(sequence) == M:
        print(*sequence)
        return
    for i in range(N):
        sequence.append(num[i])
        dfs(i)
        sequence.pop()
N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
sequence = []
dfs(0)
