import sys
input = sys.stdin.readline
x, y = map(int, input().split())
gram = [x * 1000 / y]
for _ in range(int(input())):
    a, b = map(int, input().split())
    gram.append(a * 1000 / b)
print(round(min(gram), 2))
