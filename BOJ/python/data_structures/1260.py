n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(B-A) + len(A-B))
