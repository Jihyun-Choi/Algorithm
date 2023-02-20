import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(a):
    if a == node[a]:
        return a
    p = find(node[a])
    node[a] = p
    return node[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b: return
    if a < b: node[b] = a
    else: node[a] = b

N, M = map(int,input().split())
node = [i for i in range(N+1)]
for _ in range(M):
    o, a, b = map(int,input().split())
    if o == 0: union(a,b)
    elif o == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
