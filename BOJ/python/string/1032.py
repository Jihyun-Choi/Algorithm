import sys
input = sys.stdin.readline
N = int(input())
X = list(input())
len = len(X)
for _ in range(N-1):
    Y = list(input())
    for i in range(len):
        if X[i] != Y[i]:
            X[i] = '?'
print("".join(X))
