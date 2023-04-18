word = input()
answer = []
for i in word:
    if i not in "CAMBRIDGE":
        answer.append(i)
print(*answer, sep="")
