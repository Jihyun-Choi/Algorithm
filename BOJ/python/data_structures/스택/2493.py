N = int(input())
tower = list(map(int, input().split()))
stack = []
answer= [0] * N
for i in range(N - 1, -1, -1):
    while stack and tower[stack[-1]] < tower[i]:
        answer[stack.pop()] = i + 1
    stack.append(i)
print(*answer)
