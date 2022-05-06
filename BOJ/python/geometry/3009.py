X = []
Y = []
for _ in range(3):
    x, y = map(int, input().split())
    if x in X:
        X.remove(x)
    else:
        X.append(x)
    if y in Y:
        Y.remove(y)
    else:
        Y.append(y)
x = X.pop()
y = Y.pop()
print(x, y)
