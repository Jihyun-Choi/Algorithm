N, M = map(int, input().split())
S = []
def dfs():
    if len(S) == M:
        print(*S)
        return    
    for i in range(1,N+1): 
        S.append(i)
        dfs()
        S.pop()
dfs()
