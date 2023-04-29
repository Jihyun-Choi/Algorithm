N = int(input())
A, B = map(int, input().split())
answer = A//2 + B
print(answer) if N >= answer else print(N)
