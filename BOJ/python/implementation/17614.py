N = int(input())
answer = 0
for x in range(1, N+1):
    y = x
    while y != 0:
        if (y % 10 == 3) or (y % 10 == 6) or (y % 10 == 9):
            answer += 1
        y //= 10
print(answer)
