score = [int(input()) for _ in range(8)]
index = []
sum = 0
for i in range(5):
    index.append(score.index(max(score))+1)
    sum += score[score.index(max(score))]
    score[score.index(max(score))] = 0
index.sort()
print(sum)
print(*index)
