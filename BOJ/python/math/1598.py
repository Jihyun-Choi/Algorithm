X, Y = map(int, input().split())
X, Y = X-1, Y-1
print(abs(X//4 - Y//4) + abs(X%4 - Y%4))
