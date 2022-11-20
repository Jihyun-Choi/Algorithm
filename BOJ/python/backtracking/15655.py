def dfs(idx):
    if len(sequence) == M:
        print(*sequence)
        return
    for i in range(idx, N):
        if num[i] not in sequence:
            sequence.append(num[i])
            dfs(i + 1)
            sequence.pop()
N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
sequence = []
dfs(0)
