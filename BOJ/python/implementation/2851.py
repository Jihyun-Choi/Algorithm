answer = 0
score = [int(input()) for _ in range(10)]
for i in score:
    if abs(answer+i)-100 <= abs(answer-100):
        answer += i
    else:
        break
print(answer)
