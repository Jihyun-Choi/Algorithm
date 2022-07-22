N = int(input())
A, B = 0, 0
for _ in range(N):
    X, Y = map(int, input().split())
    if X > Y:
        A += 1
    elif X < Y:
        B += 1
print(A, B)
