A, B = map(int, input().split())
X, Y = min(A, B), max(A, B)
num = [i for i in range(X+1, Y)]
print(0) if (X == Y or X+1 == Y) else print(Y-X-1)
print(*num)
