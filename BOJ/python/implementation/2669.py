rectangle = [[0 for _ in range(101)] for _ in range(101)]
answer = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if rectangle[i][j] == 0:
                rectangle[i][j] += 1
                answer += 1
print(answer)
